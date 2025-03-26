import boto3
import json
import argparse
import logging
import subprocess
import re


def select_from_list(options):
    """
    Interactively selects an option from a list.

    Args:
        options (list): A list of strings representing the options.

    Returns:
        str: The selected option, or None if no valid selection is made.
    """
    for i, option in enumerate(options):
        print(f"{i + 1}) {option}")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def auto_detect_ecs(profile_name, region):
    """
    Auto-detects and interactively selects an ECS cluster, service, and container.

    Args:
        profile_name (str): The AWS profile name.
        region (str): The AWS region.

    Returns:
        tuple: A tuple containing the selected cluster, service, and container names, or None if any selection fails.
    """
    session = boto3.Session(profile_name=profile_name, region_name=region)
    ecs_client = session.client("ecs")

    # Cluster selection
    response = ecs_client.list_clusters()
    clusters = response["clusterArns"]

    if not clusters:
        print("No ECS clusters found.")
        return None, None, None

    if len(clusters) == 1:
        cluster_arn = clusters[0]
        cluster_name = cluster_arn.split("/")[-1]
        print(f"Auto-detected cluster: {cluster_name}")
    else:
        print("Multiple clusters found. Please select one:")
        cluster_names = [arn.split("/")[-1] for arn in clusters]
        cluster_name = select_from_list(cluster_names)
        if not cluster_name:
            return None, None, None
        cluster_arn = [arn for arn in clusters if cluster_name in arn][0]

    # Service selection
    response = ecs_client.list_services(cluster=cluster_arn)
    services = response["serviceArns"]

    if not services:
        print(f"No ECS services found in cluster {cluster_name}.")
        return cluster_name, None, None

    if len(services) == 1:
        service_arn = services[0]
        service_name = service_arn.split("/")[-1]
        print(f"Auto-detected service: {service_name}")
    else:
        print("Multiple services found. Please select one:")
        service_names = [arn.split("/")[-1] for arn in services]
        service_name = select_from_list(service_names)
        if not service_name:
            return cluster_name, None, None
        service_arn = [arn for arn in services if service_name in arn][0]

    # Container selection
    response = ecs_client.list_tasks(cluster=cluster_arn, serviceName=service_name)
    tasks = response.get("taskArns", [])

    if not tasks:
        print(f"No tasks found for service {service_name} in cluster {cluster_name}.")
        return cluster_name, service_name, None

    response = ecs_client.describe_tasks(cluster=cluster_arn, tasks=[tasks[0]])
    containers = [
        c["name"]
        for c in response["tasks"][0]["containers"]
        if not re.match(r"aws-guardduty-agent.*", c["name"])
    ]

    if not containers:
        print(f"No usable containers found in service {service_name}.")
        return cluster_name, service_name, None

    if len(containers) == 1:
        container_name = containers[0]
        print(f"Auto-detected container: {container_name}")
    else:
        print("Multiple containers found. Please select one:")
        container_name = select_from_list(containers)
        if not container_name:
            return cluster_name, service_name, None

    return cluster_name, service_name, container_name

def execute_command_on_container(
    profile_name,
    region,
    cluster_name,
    service_name,
    container_name,
    command,
    dry_run=False,
):
    """
    Executes a command on a container within a specified ECS task.

    Args:
        profile_name (str): The AWS profile name.
        region (str): The AWS region.
        cluster_name (str): The name of the ECS cluster.
        service_name (str): The name of the ECS service.
        container_name (str): The name of the container.
        command (str): The command to execute.
        dry_run (bool): If True, output the AWS CLI command instead of executing.

    Returns:
        None
    """
    session = boto3.Session(profile_name=profile_name, region_name=region)
    ecs_client = session.client("ecs")

    # Get the task ARN
    try:
        logging.debug(
            f"Boto3 ECS list_tasks call: ecs_client.list_tasks(cluster='{cluster_name}', serviceName='{service_name}')"
        )
        response = ecs_client.list_tasks(cluster=cluster_name, serviceName=service_name)
        logging.debug(f"Full response from list_tasks: {response}")
        tasks = response.get("taskArns", [])
    except Exception as e:
        logging.error(f"Error during list_tasks: {e}")
        return

    if not tasks:
        print(f"No tasks found for service {service_name} in cluster {cluster_name}.")
        return

    task_arn = tasks[0]

    if dry_run:
        print(
            f"aws ecs execute-command --cluster {cluster_name} --task {task_arn} --container {container_name} --interactive --command '{command}' --region {region} --profile {profile_name}"
        )
        return

    # Execute the command using subprocess (for interactive sessions)
    try:
        cmd = [
            "aws",
            "ecs",
            "execute-command",
            "--cluster", cluster_name,
            "--task", task_arn,
            "--container", container_name,
            "--interactive",
            "--command", command,
            "--region", region,
            "--profile", profile_name,
        ]

        logging.debug(f"Executing command: {cmd}")

        process = subprocess.Popen(cmd)
        process.wait()  # Wait for the process to complete.

    except FileNotFoundError:
        logging.error("aws command not found. Ensure the aws cli is installed.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="Execute commands on ECS containers.")
    parser.add_argument("-p", "--profile", required=True, help="AWS profile name.")
    parser.add_argument(
        "-r", "--region", default="us-west-2", help="AWS region (default: us-west-2)."
    )
    parser.add_argument(
        "-c",
        "--command",
        default="/bin/bash",
        help="Command to execute (default: /bin/bash).",
    )
    parser.add_argument("--cluster", help="ECS cluster name (optional).")
    parser.add_argument("--service", help="ECS service name (optional).")
    parser.add_argument("--container", help="Container name (optional).")
    parser.add_argument(
        "-d",
        "--dry-run",
        action="store_true",
        help="Output the AWS CLI command instead of executing.",
    )
    parser.add_argument(
        "-l",
        "--log-level",
        default="WARNING",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: WARNING).",
    )

    args = parser.parse_args()

    # Configure logging based on the provided log level
    logging.basicConfig(level=getattr(logging, args.log_level.upper()))

    cluster = args.cluster
    service = args.service
    container = args.container
    command = args.command

    if not cluster or not service or not container:
        cluster, service, container = auto_detect_ecs(args.profile, args.region)
        if not cluster or not service or not container:
            return

    execute_command_on_container(
        args.profile, args.region, cluster, service, container, command, args.dry_run
    )


if __name__ == "__main__":
    main()

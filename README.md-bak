# aws_util

A collection of AWS utility functions for Python

## Description

`aws_util` provides a set of helpful functions to simplify common tasks when
working with AWS  Services. It currently includes functionality to execute
commands within running containers.


## Installation

**TL;DR: Run `source activate.sh` to set up your development environment. This creates an isolated virtual environment, installs `aws_util` and its dependencies, and updates `pip`. After installation, you can run `ecs_connect -p <your_profile>` to connect to an ECS container.**

**Virtual Environment Isolation:** The installation process creates an isolated virtual environment (`venv`). This environment ensures that `aws_util` and its dependencies are installed separately from your system's Python packages, preventing conflicts and keeping your system clean.

local installation in a virtual environment can be done using:

```bash
source venv.sh 
```

* Now you can use the `ecs_connect` command to run your script.
* **Important:** You need to provide your AWS profile.

```bash
ecs_connect -p your_aws_profile
```

* Replace `your_aws_profile` and optionally `your_aws_region` with your actual AWS profile name and region.
* Example:

```bash
ecs_connect -p my-dev-profile -r us-east-1
```

## Usage

After installation, you can directly execute commands on an ECS container using the `ecs_connect` command.

Example:

```bash
ecs_connect -p your_aws_profile
```

This will open an interactive bash shell in the selected ECS container.

For more options, check the help message:

```bash
ecs_connect --help
```

## Troubleshooting

* **"command not found: ecs_connect"**:
    * Make sure you activated the virtual environment (if you created one).
    * Make sure you ran the `pip install -e .` command.
* **"ModuleNotFoundError: No module named 'boto3'"**:
    * Make sure you activated the virtual environment and ran the `pip install -e .` command.
* **"Error with AWS credentials"**:
    * Make sure your AWS CLI is configured correctly.
    * Make sure the profile you are using is valid.
* **"Error with arguments"**:
    * Double check that you are using the correct arguments.
    * Double check that you are using the correct values for the arguments.

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes.
4.  Commit your changes and push them to your fork.
5.  Submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.



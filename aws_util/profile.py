import argparse
import boto3
import sys

def get_aws_profiles():
    """Retrieves a list of available AWS profiles."""
    try:
        session = boto3.Session()
        return session.available_profiles
    except Exception as e:
        print(f"Error retrieving AWS profiles: {e}")
        return []

def complete_profiles(prefix):
    """Filters AWS profiles based on a prefix."""
    profiles = get_aws_profiles()
    if not prefix:
        return profiles
    parts = list(prefix.lower())

    filtered_profiles = []
    for profile in profiles:
        lower_profile = profile.lower()
        valid = True
        for part in parts:
            if part not in lower_profile:
                valid = False
                break
            lower_profile = lower_profile[lower_profile.index(part)+1:]

        if valid:
            filtered_profiles.append(profile)

    return filtered_profiles

def main():
    parser = argparse.ArgumentParser(description="AWS Profile Completion.")
    parser.add_argument(
        "-p", "--profile", help="AWS profile name", nargs='?'
    )

    args = parser.parse_args()

    if args.profile is not None:
        profiles = complete_profiles(args.profile)
        if len(profiles) > 0:
            print(" ".join(profiles))
        sys.exit(0)
    else:
        profiles = get_aws_profiles()
        print(" ".join(profiles))
        sys.exit(0)

if __name__ == "__main__":
    main()

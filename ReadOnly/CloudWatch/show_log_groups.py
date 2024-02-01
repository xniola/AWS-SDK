import boto3

def list_cloudwatch_log_groups(profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=profile)

    # Create a Boto3 client for CloudWatch Logs using the session
    cloudwatch_logs_client = session.client('logs')

    # Get a list of all CloudWatch log groups
    response = cloudwatch_logs_client.describe_log_groups()

    # Display the log group names
    print("CloudWatch Log Groups:")
    for log_group in response['logGroups']:
        print(f"  {log_group['logGroupName']}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List all CloudWatch log groups")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()

    # Call the function to list CloudWatch log groups
    list_cloudwatch_log_groups(args.profile)

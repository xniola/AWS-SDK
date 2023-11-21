import boto3

def list_scheduled_eventbridge_rules(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for EventBridge using the session
    eventbridge_client = session.client('scheduler')

    try:
        # List EventBridge schedules
        response = eventbridge_client.list_schedules()

        # Iterate through the schedules and print details
        for schedule in response['Schedules']:
            print(f"Schedule Name: {schedule['Name']}")
            print(f"Schedule Arn: {schedule['Arn']}")
            print(f"State: {schedule['State']}")
            print(f"Target: {schedule['Target']['Arn']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List EventBridge Schedules")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_scheduled_eventbridge_rules(args.profile)

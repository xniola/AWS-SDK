import boto3

def list_eventbridge_rules(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for EventBridge using the session
    eventbridge_client = session.client('events')

    try:
        # List EventBridge rules
        response = eventbridge_client.list_rules()

        # Iterate through the rules and print their details
        for rule in response['Rules']:
            print(f"Rule Name: {rule['Name']}")
            print(f"Rule ARN: {rule['Arn']}")
            print(f"State: {rule['State']}")

            try:
                print(f"Description: {rule['Description']}")
            except Exception:
                pass

            try:
                print(f"Schedule: {rule['ScheduleExpression']}")
            except Exception:
                print(f"Event: {rule['EventPattern']}")

            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List EventBridge Rules")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_eventbridge_rules(args.profile)

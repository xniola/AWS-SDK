import boto3

def list_iam_groups(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for IAM using the session
    iam_client = session.client('iam')

    try:
        # List IAM groups
        response = iam_client.list_groups()

        # Iterate through the groups and print their details
        for group in response['Groups']:
            print(f"IAM Group Name: {group['GroupName']}")
            print(f"IAM Group ARN: {group['Arn']}")
            print(f"Creation Date: {group['CreateDate']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List IAM Groups")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_iam_groups(args.profile)

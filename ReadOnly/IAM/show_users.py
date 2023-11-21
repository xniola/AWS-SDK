import boto3

def list_iam_users(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for IAM using the session
    iam_client = session.client('iam')

    try:
        # List IAM users
        response = iam_client.list_users()

        # Iterate through the users and print their details
        for user in response['Users']:
            print(f"IAM User Name: {user['UserName']}")
            print(f"IAM User ARN: {user['Arn']}")
            print(f"User ID: {user['UserId']}")
            print(f"Creation Date: {user['CreateDate']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List IAM Users")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_iam_users(args.profile)

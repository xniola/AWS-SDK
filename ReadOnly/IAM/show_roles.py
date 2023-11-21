import boto3

def list_iam_roles(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for IAM using the session
    iam_client = session.client('iam')
    findings = 0

    try:
        # List IAM roles
        response = iam_client.list_roles()

        # Iterate through the roles and print their details
        for role in response['Roles']:
            findings += 1
            print(f"IAM Role Name: {role['RoleName']}")
            print(f"IAM Role ARN: {role['Arn']}")
            print(f"Creation Date: {role['CreateDate']}")
            print()

        print("Total findings: "+str(findings))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List IAM Roles")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_iam_roles(args.profile)

import boto3

def list_iam_policies(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for IAM using the session
    iam_client = session.client('iam')
    findings = 0

    try:
        # List IAM policies
        response = iam_client.list_policies(Scope='All')

        # Iterate through the policies and print their details
        for policy in response['Policies']:
            findings += 1
            print(f"IAM Policy Name: {policy['PolicyName']}")
            print(f"IAM Policy ARN: {policy['Arn']}")
            print(f"Policy ID: {policy['PolicyId']}")
            print(f"Default Version ID: {policy['DefaultVersionId']}")
            print(f"Attachment Count: {policy['AttachmentCount']}")
            print(f"Is Attachable: {policy['IsAttachable']}")
            print()

        print("Total findings: "+str(findings))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List IAM Policies")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_iam_policies(args.profile)

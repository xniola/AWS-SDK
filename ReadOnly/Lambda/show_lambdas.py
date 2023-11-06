import boto3

def list_lambda_functions(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for AWS Lambda using the session
    lambda_client = session.client('lambda')

    try:
        # List Lambda functions
        response = lambda_client.list_functions()

        # Iterate through the Lambda functions and print their details
        for function in response['Functions']:
            print(f"Function Name: {function['FunctionName']}")
            print(f"Runtime: {function['Runtime']}")
            print(f"Last Modified: {function['LastModified']}")
            print(f"Handler: {function['Handler']}")
            print(f"Role: {function['Role']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List AWS Lambda Functions")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_lambda_functions(args.profile)

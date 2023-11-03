import boto3

def get_lambda_function_details(aws_profile, function_name):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for AWS Lambda using the session
    lambda_client = session.client('lambda')

    try:
        # Get details of the specific Lambda function
        response = lambda_client.get_function(FunctionName=function_name)

        # Print the details of the Lambda function
        print(f"Function Name: {response['Configuration']['FunctionName']}")
        print(f"Runtime: {response['Configuration']['Runtime']}")
        print(f"Last Modified: {response['Configuration']['LastModified']}")
        print(f"Handler: {response['Configuration']['Handler']}")
        print(f"Role: {response['Configuration']['Role']}")
        print(f"Description: {response['Configuration']['Description']}")
        print()

    except lambda_client.exceptions.ResourceNotFoundException:
        print(f"Lambda function '{function_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Get AWS Lambda Function Details")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--function_name", type=str, required=True, help="Name of the Lambda function")

    args = parser.parse_args()
    get_lambda_function_details(args.profile, args.function_name)

import boto3

def get_lambda_function_details(aws_profile, function_name, region):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile, region_name=region)

    # Create a Boto3 client for AWS Lambda using the session
    lambda_client = session.client('lambda')

    try:
        # Get details of the specific Lambda function
        response = lambda_client.get_function(FunctionName=function_name)

        # Extract relevant details from the response
        function_details = response['Configuration']

        # Print the details of the Lambda function
        print(f"Function Name: {function_details['FunctionName']}")
        print(f"Runtime: {function_details['Runtime']}")
        print(f"Last Modified: {function_details['LastModified']}")
        print(f"Handler: {function_details['Handler']}")
        print(f"Role: {function_details['Role']}")
        print(f"Description: {function_details['Description']}")
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
    parser.add_argument("--region", type=str, required=True, help="AWS region")

    args = parser.parse_args()
    get_lambda_function_details(args.profile, args.function_name, args.region)

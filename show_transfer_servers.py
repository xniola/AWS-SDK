import boto3

def list_transfer_servers(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for AWS Transfer Family using the session
    transfer_client = session.client('transfer')

    try:
        # List Transfer Family servers
        response = transfer_client.list_servers()

        # Iterate through the servers and print their details
        for server in response['Servers']:
            print(f"Server ID: {server['ServerId']}")
            print(f"ARN: {server['Arn']}")
            print(f"Domain: {server['Domain']}")
            print(f"Identity Provider: {server['IdentityProviderType']}")
            print(f"Server State: {server['State']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List AWS Transfer Family Servers")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_transfer_servers(args.profile)

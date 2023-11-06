import boto3

def list_all_network_interfaces(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for EC2 using the session
    ec2 = session.client('ec2')

    try:
        # Describe all network interfaces in your AWS account
        response = ec2.describe_network_interfaces()

        # Iterate through the network interfaces and print their details
        for network_interface in response['NetworkInterfaces']:
            print(f"Network Interface ID: {network_interface['NetworkInterfaceId']}")
            print(f"Status: {network_interface['Status']}")
            try:
                print(f"Attachment ID: {network_interface['Attachment']['AttachmentId']}")
            except Exception:
                print(f"Attachment ID: not attached ({network_interface['Description']})")
            print(f"MAC Address: {network_interface['MacAddress']}")
            print(f"Private IP Address: {network_interface['PrivateIpAddress']}")
            print(f"VPC ID: {network_interface['VpcId']}")
            print()

    except ec2.exceptions.ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List All Network Interfaces in Your AWS Account")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_all_network_interfaces(args.profile)

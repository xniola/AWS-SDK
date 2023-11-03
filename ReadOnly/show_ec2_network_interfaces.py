import boto3

def list_network_interfaces(aws_profile, instance_id):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for EC2 using the session
    ec2 = session.client('ec2')

    try:
        # Describe the network interfaces of the specified EC2 instance
        response = ec2.describe_network_interfaces(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}])

        # Iterate through the network interfaces and print their details
        for network_interface in response['NetworkInterfaces']:
            print(f"Network Interface ID: {network_interface['NetworkInterfaceId']}")
            print(f"Status: {network_interface['Status']}")
            print(f"Attachment ID: {network_interface['Attachment']['AttachmentId']}")
            print(f"MAC Address: {network_interface['MacAddress']}")
            print(f"Private IP Address: {network_interface['PrivateIpAddress']}")
            print(f"VPC ID: {network_interface['VpcId']}")
            print()

    except ec2.exceptions.ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List Network Interfaces of an EC2 Instance")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--instance-id", type=str, required=True, help="EC2 instance ID")

    args = parser.parse_args()
    list_network_interfaces(args.profile, args.instance_id)

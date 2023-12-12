import argparse
import boto3

def list_allocation_ips(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2 = session.client('ec2')

    response = ec2.describe_addresses()

    for address in response['Addresses']:
        allocation_id = address.get('AllocationId', 'N/A')
        public_ip = address.get('PublicIp', 'N/A')
        instance_id = address.get('InstanceId', 'N/A')
        association_id = address.get('AssociationId', 'N/A')
        domain = address.get('Domain', 'N/A')

        print(f"Allocation ID: {allocation_id}")
        print(f"Public IP: {public_ip}")
        print(f"Instance ID: {instance_id}")
        print(f"Association ID: {association_id}")
        print(f"Domain: {domain}")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List Allocation IPs")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_allocation_ips(args.profile)


import argparse
import boto3

def list_subnets(vpc_id, aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2 = session.client('ec2')

    try:
        response = ec2.describe_subnets(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])

        for subnet in response['Subnets']:
            print(f"Subnet ID: {subnet['SubnetId']}")
            print(f"Subnet Name: {subnet['Tags'][0]['Value'] if 'Tags' in subnet else 'N/A'}")
            print(f"Availability Zone: {subnet['AvailabilityZone']}")
            print(f"CIDR Block: {subnet['CidrBlock']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List subnets in a VPC")
    parser.add_argument("--vpc_id", type=str, help="VPC ID")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_subnets(args.vpc_id, args.profile)

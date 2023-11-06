import argparse
import boto3

def get_instance_name(instance):
    for tag in instance.get('Tags', []):
        if tag['Key'] == 'Name':
            return tag['Value']
    return 'N/A'

def list_instances(display_all,aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2 = session.client('ec2')

    if display_all:
        filters = []  # No filters, display all instances
    else:
        print("***")
        print("N.B. To show also non running instances run the command with --all option")
        print("***\n")
        filters = [
            {
                'Name': 'instance-state-name',
                'Values': ['running'],
            }
        ]

    response = ec2.describe_instances(Filters=filters)

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_name =get_instance_name(instance)
            vpc_id = instance['VpcId']
            subnet_id = instance['SubnetId']
            vpc_response = ec2.describe_vpcs(VpcIds=[vpc_id])
            vpc = vpc_response['Vpcs'][0] if vpc_response['Vpcs'] else None
            subnet_response = ec2.describe_subnets(SubnetIds=[subnet_id])
            subnet = subnet_response['Subnets'][0] if subnet_response['Subnets'] else None
            print(f"Instance Name: {instance_name}")
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"Public IP Address: {instance.get('PublicIpAddress', 'N/A')}")
            print(f"Private IP Address: {instance.get('PrivateIpAddress', 'N/A')}")
            print(f"VPC Name: {vpc['Tags'][0]['Value'] if vpc and 'Tags' in vpc else 'N/A'} ({vpc_id})")
            print(f"Subnet Name: {subnet['Tags'][0]['Value'] if subnet and 'Tags' in subnet else 'N/A'} ({subnet_id})")
            print(f"State: {instance['State']['Name']}")
            print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List EC2 instances")
    parser.add_argument("--all", action="store_true", help="Display all instances (including stopped ones)")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_instances(args.all,args.profile)


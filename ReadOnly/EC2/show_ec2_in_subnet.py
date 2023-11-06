import argparse
import boto3

def get_instance_name(instance):
    for tag in instance.get('Tags', []):
        if tag['Key'] == 'Name':
            return tag['Value']
    return 'N/A'

def list_instances_in_subnet(subnet_id, aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2 = session.client('ec2')

    try:
        response = ec2.describe_instances(Filters=[{'Name': 'subnet-id', 'Values': [subnet_id]}])

        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_name = get_instance_name(instance)
                print(f"Instance Name: {instance_name}")
                print(f"Instance ID: {instance['InstanceId']}")
                print(f"Instance Type: {instance['InstanceType']}")
                print(f"Public IP Address: {instance.get('PublicIpAddress', 'N/A')}")
                print(f"Private IP Address: {instance.get('PrivateIpAddress', 'N/A')}")
                print(f"State: {instance['State']['Name']}")
                print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List instances in a subnet")
    parser.add_argument("--subnet_id", type=str, help="Subnet ID")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_instances_in_subnet(args.subnet_id, args.profile)

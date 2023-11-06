import argparse
import boto3

def list_instance_store_instances(profile_name):
    # Initialize the Boto3 EC2 client with the specified profile
    session = boto3.Session(profile_name=profile_name)
    ec2_client = session.client('ec2')

    # List EC2 instances with instance store volumes
    filters = [
        {'Name': 'block-device-mapping.device-name', 'Values': ['/dev/sda1']},
        {'Name': 'instance-state-name', 'Values': ['running']},
    ]

    instances = ec2_client.describe_instances(Filters=filters)

    # Print information about each instance
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            print(f"Instance ID: {instance['InstanceId']}")
            print(f"Instance Type: {instance['InstanceType']}")
            print(f"Availability Zone: {instance['Placement']['AvailabilityZone']}")
            print(f"State: {instance['State']['Name']}")
            print()

def main():
    parser = argparse.ArgumentParser(description='List EC2 Instances with Instance Store Volumes')
    parser.add_argument('--profile', help='AWS CLI profile name', required=True)

    args = parser.parse_args()
    list_instance_store_instances(args.profile)

if __name__ == '__main__':
    main()

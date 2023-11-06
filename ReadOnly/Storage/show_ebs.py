import argparse
import boto3

def list_ebs_volumes(profile_name):
    # Initialize the Boto3 EC2 client with the specified profile
    session = boto3.Session(profile_name=profile_name)
    ec2_client = session.client('ec2')

    # List EBS volumes
    volumes = ec2_client.describe_volumes()

    # Print information about each volume
    for volume in volumes['Volumes']:
        print(f"Volume ID: {volume['VolumeId']}")
        print(f"Size (GiB): {volume['Size']} GiB")
        print(f"Availability Zone: {volume['AvailabilityZone']}")
        print(f"State: {volume['State']}")
        print()

def main():
    parser = argparse.ArgumentParser(description='List EBS Volumes')
    parser.add_argument('--profile', help='AWS CLI profile name', required=True)

    args = parser.parse_args()
    list_ebs_volumes(args.profile)

if __name__ == '__main__':
    main()

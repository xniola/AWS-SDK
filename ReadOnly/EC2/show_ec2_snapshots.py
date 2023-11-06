import argparse
import boto3

def list_ec2_snapshots(profile_name):
    # Initialize the Boto3 EC2 client with the specified profile
    session = boto3.Session(profile_name=profile_name)
    ec2_client = session.client('ec2')

    # List EC2 snapshots
    snapshots = ec2_client.describe_snapshots(OwnerIds=['self'])
    
    # Print information about each snapshot
    for snapshot in snapshots['Snapshots']:
        print(f"Snapshot ID: {snapshot['SnapshotId']}")
        print(f"Volume ID: {snapshot['VolumeId']}")
        print(f"Start Time: {snapshot['StartTime']}")
        print(f"Progress: {snapshot['Progress']}")
        print(f"State: {snapshot['State']}")
        print()

def main():
    parser = argparse.ArgumentParser(description='List EC2 Snapshots')
    parser.add_argument('--profile', help='AWS CLI profile name', required=True)
    
    args = parser.parse_args()
    list_ec2_snapshots(args.profile)

if __name__ == '__main__':
    main()

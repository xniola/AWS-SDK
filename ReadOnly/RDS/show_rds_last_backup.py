import argparse
import boto3

def list_last_system_snapshot(profile_name, db_instance_identifier):
    # Initialize the Boto3 RDS client with the specified profile
    session = boto3.Session(profile_name=profile_name)
    rds_client = session.client('rds')

    # Get all snapshots for the specified DB instance
    response = rds_client.describe_db_snapshots(
        DBInstanceIdentifier=db_instance_identifier,
        SnapshotType='automated'
    )

    # Sort snapshots by the 'SnapshotCreateTime' in descending order
    snapshots = sorted(response['DBSnapshots'], key=lambda x: x['SnapshotCreateTime'], reverse=True)

    if snapshots:
        # Print information about the latest system snapshot
        latest_system_snapshot = snapshots[0]
        print(latest_system_snapshot)
        exit(0)
        print("Latest System Snapshot:")
        print(f"Snapshot ID: {latest_system_snapshot['DBSnapshotIdentifier']}")
        print(f"Snapshot Type: {latest_system_snapshot['SnapshotType']}")
        print(f"Snapshot Create Time: {latest_system_snapshot['SnapshotCreateTime']}")
    else:
        print("No automated system snapshots found for the specified DB instance.")

def main():
    parser = argparse.ArgumentParser(description='List Last RDS System Snapshot')
    parser.add_argument('--profile', help='AWS CLI profile name', required=True)
    parser.add_argument('--db-instance-identifier', help='DB instance identifier', required=True)

    args = parser.parse_args()
    list_last_system_snapshot(args.profile, args.db_instance_identifier)

if __name__ == '__main__':
    main()

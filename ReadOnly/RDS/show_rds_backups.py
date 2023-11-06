import argparse
import boto3

def list_rds_backups(profile_name):
    # Initialize the Boto3 RDS client with the specified profile
    session = boto3.Session(profile_name=profile_name)
    rds_client = session.client('rds')

    # List RDS DB backups
    backups = rds_client.describe_db_snapshots()
    
    # Print information about each backup
    for backup in backups['DBSnapshots']:
        print(f"DB Snapshot ID: {backup['DBSnapshotIdentifier']}")
        print(f"DB Instance Identifier: {backup['DBInstanceIdentifier']}")
        print(f"Snapshot Creation Time: {backup['SnapshotCreateTime']}")
        print(f"Status: {backup['Status']}")
        print(f"Backup Type: {backup['SnapshotType']}")
        print()

def main():
    parser = argparse.ArgumentParser(description='List RDS Backups')
    parser.add_argument('--profile', help='AWS CLI profile name', required=True)
    
    args = parser.parse_args()
    list_rds_backups(args.profile)

if __name__ == '__main__':
    main()

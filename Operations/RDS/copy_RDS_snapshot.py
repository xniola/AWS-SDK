import boto3

def copy_rds_snapshot(source_region, source_snapshot_arn, target_region, target_snapshot_identifier):
    # Create RDS clients for source and target regions
    source_rds_client = boto3.client('rds', region_name=source_region)
    target_rds_client = boto3.client('rds', region_name=target_region)

    # Copy the snapshot to the target region
    response = target_rds_client.copy_db_snapshot(
        SourceDBSnapshotIdentifier=source_snapshot_arn,
        TargetDBSnapshotIdentifier=target_snapshot_identifier,
        SourceRegion=source_region
    )

    # Wait for the snapshot copy to complete
    target_rds_client.get_waiter('db_snapshot_available').wait(
        DBSnapshotIdentifier=target_snapshot_identifier,
        WaiterConfig={'Delay': 30, 'MaxAttempts': 60}
    )

    print(f"Snapshot {target_snapshot_identifier} copied to {target_region}.")

# Replace these values with your actual details
source_region = 'us-east-1'
source_snapshot_arn = 'arn:aws:rds:us-east-1:account-id:snapshot:your-source-snapshot-id'
target_region = 'us-west-2'
target_snapshot_identifier = 'your-target-snapshot-id'

copy_rds_snapshot(source_region, source_snapshot_arn, target_region, target_snapshot_identifier)

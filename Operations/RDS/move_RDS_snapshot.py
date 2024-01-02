import boto3

def copy_rds_snapshot(source_region, source_snapshot_arn, target_region, target_snapshot_identifier):
    # Create RDS clients for source and target regions
    source_rds_client = boto3.client('rds', region_name=source_region)
    target_rds_client = boto3.client('rds', region_name=target_region)

    try:
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

        print(f"Snapshot {source_snapshot_arn} copied to {target_region} with identifier {target_snapshot_identifier}.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Copy RDS Snapshot to Another Region")
    parser.add_argument("--source_region", type=str, required=True, help="Source AWS region")
    parser.add_argument("--source_snapshot_arn", type=str, required=True, help="Source snapshot ARN")
    parser.add_argument("--target_region", type=str, required=True, help="Target AWS region")
    parser.add_argument("--target_snapshot_identifier", type=str, required=True, help="Target snapshot identifier")

    args = parser.parse_args()
    copy_rds_snapshot(args.source_region, args.source_snapshot_arn, args.target_region, args.target_snapshot_identifier)

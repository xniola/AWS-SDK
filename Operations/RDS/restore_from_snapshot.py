import json
import boto3
import os


def get_last_system_snapshot(db_identifier):
    rds_client = boto3.client('rds')

    # Retrieve all snapshots of the specified DB in descending order of creation time
    response = rds_client.describe_db_snapshots(
        DBInstanceIdentifier=db_identifier,
        SnapshotType='automated'
    )

    snapshots = sorted(response['DBSnapshots'], key=lambda x: x['SnapshotCreateTime'], reverse=True)

    if snapshots:
        return snapshots[0]['DBSnapshotIdentifier'], snapshots[0]['DBSnapshotArn']
    else:
        return None

def restore_rds_snapshot(snapshot_identifier, instance_identifier, instance_class, subnet_group_name, security_group_ids, engine):
    rds_client = boto3.client('rds')

    response = rds_client.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=instance_identifier,
        DBSnapshotIdentifier=snapshot_identifier,
        DBInstanceClass=instance_class,
        Port=1433,
        AvailabilityZone='eu-central-1b',
        DBSubnetGroupName=subnet_group_name,
        MultiAZ=False,
        PubliclyAccessible=False,
        VpcSecurityGroupIds=[security_group_ids],
        Engine=engine,
        Iops=2000,
        OptionGroupName='emerald-db-option-group'
    )

    print(f"Restoring snapshot {snapshot_identifier}.")

def lambda_handler(event, context):
    # Replace these values with your actual environment variable names
    db_identifier = os.environ.get('db_identifier')
    instance_identifier = os.environ.get('instance_identifier')
    instance_class = os.environ.get('instance_class')
    subnet_group_name = os.environ.get('subnet_group_name')
    security_group_ids = os.environ.get('security_group_ids')
    engine = os.environ.get('engine')

    snapshot_identifier, snapshot_arn = get_last_system_snapshot(db_identifier)

    if snapshot_identifier is not None:
        restore_rds_snapshot(snapshot_identifier, instance_identifier, instance_class, subnet_group_name, security_group_ids, engine)

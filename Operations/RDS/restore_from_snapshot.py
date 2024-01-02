import boto3

def restore_rds_snapshot(snapshot_identifier, instance_identifier, subnet_group_name, security_group_ids, engine, instance_class, username, password):
    rds_client = boto3.client('rds')

    response = rds_client.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=instance_identifier,
        DBSnapshotIdentifier=snapshot_identifier,
        DBSubnetGroupName=subnet_group_name,
        VpcSecurityGroupIds=security_group_ids,
        Engine=engine,
        DBInstanceClass=instance_class,
        MasterUsername=username,
        MasterUserPassword=password
    )

    print(f"Restoring RDS instance {instance_identifier} from snapshot {snapshot_identifier}.")
    print("Please wait for the restoration to complete.")

    # Optionally, you can wait for the restoration to complete
    waiter = rds_client.get_waiter('db_instance_available')
    waiter.wait(DBInstanceIdentifier=instance_identifier)

    print(f"RDS instance {instance_identifier} has been successfully restored.")

# Replace these values with your actual details
snapshot_identifier = 'your-snapshot-id'
instance_identifier = 'your-instance-id'
subnet_group_name = 'your-subnet-group-name'
security_group_ids = ['sg-xxxxxxxx']
engine = 'your-db-engine'
instance_class = 'db.t2.micro'
username = 'your-db-username'
password = 'your-db-password'

restore_rds_snapshot(snapshot_identifier, instance_identifier, subnet_group_name, security_group_ids, engine, instance_class, username, password)

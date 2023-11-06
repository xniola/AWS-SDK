import boto3

def start_rds_instance(aws_profile, instance_identifier):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for RDS using the session
    rds = session.client('rds')

    try:
        # Start the RDS instance
        response = rds.start_db_instance(DBInstanceIdentifier=instance_identifier)

        # Check the status of the instance to ensure it's starting
        instance_status = response['DBInstance']['DBInstanceStatus']
        print(f"Started RDS instance '{instance_identifier}' (Status: {instance_status})")

    except rds.exceptions.DBInstanceNotFoundFault:
        print(f"RDS instance '{instance_identifier}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Start an RDS Instance")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--instance-identifier", type=str, required=True, help="RDS instance identifier")

    args = parser.parse_args()
    start_rds_instance(args.profile, args.instance_identifier)

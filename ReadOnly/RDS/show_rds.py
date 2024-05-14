import boto3
import argparse

def list_rds_instances(aws_profile):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for RDS using the session
    rds = session.client('rds')

    try:
        # List RDS instances
        response = rds.describe_db_instances()
        
        # Iterate through the RDS instances and print their details
        for instance in response['DBInstances']:
            print(f"Instance Identifier: {instance['DBInstanceIdentifier']}")
            print(f"Class: {instance['DBInstanceClass']}")
            print(f"Port: {instance['Endpoint']['Port']}")
            print(f"Storage: {instance['AllocatedStorage']} GB")
            print(f"Engine: {instance['Engine']}")
            print(f"Instance Status: {instance['DBInstanceStatus']}")
            print(f"Endpoint: {instance['Endpoint']['Address']}")
            print()
            

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List RDS Instances")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")

    args = parser.parse_args()
    list_rds_instances(args.profile)

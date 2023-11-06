import boto3

def stop_ec2_instance(aws_profile, instance_id):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for EC2 using the session
    ec2 = session.client('ec2')

    try:
        # Stop the EC2 instance
        response = ec2.stop_instances(InstanceIds=[instance_id])

        # Check the state of the instance to ensure it's stopping
        instance_state = response['StoppingInstances'][0]['CurrentState']['Name']
        print(f"Stopping EC2 instance '{instance_id}' (State: {instance_state})")

    except ec2.exceptions.InstanceNotFound:
        print(f"EC2 instance '{instance_id}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Stop an EC2 Instance")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--instance-id", type=str, required=True, help="EC2 instance ID")

    args = parser.parse_args()
    stop_ec2_instance(args.profile, args.instance_id)

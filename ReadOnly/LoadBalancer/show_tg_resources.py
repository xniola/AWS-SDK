import argparse
import boto3

def list_target_group_resources(aws_profile, target_group_arn):
    session = boto3.Session(profile_name=aws_profile)
    elbv2 = session.client('elbv2')

    response = elbv2.describe_target_health(TargetGroupArn=target_group_arn)

    print(f"Resources in Target Group (ARN: {target_group_arn}):")
    for target_health in response['TargetHealthDescriptions']:
        target_id = target_health['Target']['Id']
        target_port = target_health['Target']['Port']
        health_state = target_health['TargetHealth']['State']
        reason = target_health['TargetHealth'].get('Reason', 'N/A')
        description = target_health.get('Description', 'N/A')

        print(f"Target ID: {target_id}")
        print(f"Target Port: {target_port}")
        print(f"Health State: {health_state}")
        print(f"Reason: {reason}")
        print(f"Description: {description}")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List Resources in a Target Group")
    parser.add_argument("--profile", type=str, help="AWS profile name")
    parser.add_argument("--target-group-arn", type=str, help="Target Group ARN")

    args = parser.parse_args()
    list_target_group_resources(args.profile, args.target_group_arn)

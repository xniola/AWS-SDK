import argparse
import boto3

def list_target_groups(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    elbv2 = session.client('elbv2')

    response = elbv2.describe_target_groups()

    for target_group in response['TargetGroups']:
        tg_name = target_group['TargetGroupName']
        tg_arn = target_group['TargetGroupArn']
        tg_protocol = target_group['Protocol']
        tg_port = target_group['Port']
        tg_vpc_id = target_group['VpcId']
        health_check_path = target_group['HealthCheckPath']  # Added this line

        print(f"Target Group Name: {tg_name}")
        print(f"Target Group ARN: {tg_arn}")
        print(f"Protocol: {tg_protocol}")
        print(f"Port: {tg_port}")
        print(f"VPC ID: {tg_vpc_id}")
        print(f"Health Check Path: {health_check_path}")  # Added this line
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List Target Groups")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_target_groups(args.profile)

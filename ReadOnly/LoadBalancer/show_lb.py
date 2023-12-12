import argparse
import boto3

def list_load_balancers(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    elbv2 = session.client('elbv2')

    response = elbv2.describe_load_balancers()

    for lb in response['LoadBalancers']:
        lb_name = lb['LoadBalancerName']
        lb_arn = lb['LoadBalancerArn']
        lb_dns = lb['DNSName']
        lb_type = lb['Type']
        lb_scheme = lb['Scheme']
        print(f"Load Balancer Name: {lb_name}")
        print(f"Load Balancer ARN: {lb_arn}")
        print(f"DNS Name: {lb_dns}")
        print(f"Type: {lb_type}")
        print(f"Scheme: {lb_scheme}")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List Load Balancers")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_load_balancers(args.profile)


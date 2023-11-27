import argparse
import boto3

def list_transit_gateways(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2 = session.client('ec2')

    try:
        response = ec2.describe_transit_gateways()

        for transit_gateway in response['TransitGateways']:
            print(f"Transit Gateway ID: {transit_gateway['TransitGatewayId']}")
            print(f"Transit Gateway State: {transit_gateway['State']}")
            print(f"Amazon Side ASN: {transit_gateway.get('AmazonSideAsn', 'N/A')}")
            print(f"Creation Time: {transit_gateway['CreationTime']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List Transit Gateways")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_transit_gateways(args.profile)

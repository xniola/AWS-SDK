import argparse
import boto3

def list_client_vpn_endpoints(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2_client = session.client('ec2')

    response = ec2_client.describe_client_vpn_endpoints()

    for endpoint in response['ClientVpnEndpoints']:
        print(f"Client VPN Endpoint ID: {endpoint['ClientVpnEndpointId']}")
        #print(f"ARN: {endpoint['ClientVpnEndpointArn']}")
        print(f"Description: {endpoint.get('Description', 'N/A')}")
        print(f"Status: {endpoint['Status']['Code']}")
        print(f"DNS Name: {endpoint['DnsName']}")
        print(f"Client CIDR Block: {endpoint['ClientCidrBlock']}")
        print(f"Creation Time: {endpoint['CreationTime']}")
        print(f"Deletion Time: {endpoint.get('DeletionTime', 'N/A')}")
        print(f"Split Tunnel: {endpoint['SplitTunnel']}")
        print(f"Authentication Options:")
        for auth_option in endpoint['AuthenticationOptions']:
            print(f"  - Type: {auth_option['Type']}")
            print(f"    Active Directory ID: {auth_option.get('ActiveDirectoryId', 'N/A')}")
            print()
        
        # Fetch and print network associations
        print("Network Associations:")
        associations = ec2_client.describe_client_vpn_target_networks(ClientVpnEndpointId=endpoint['ClientVpnEndpointId'])
        for association in associations['ClientVpnTargetNetworks']:
            print(f"  - VPC ID: {association['VpcId']}")
            print(f"    Security Groups: {association['SecurityGroups']}")
            print(f"    Status: {association['Status']['Code']}")
            print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List AWS Client VPN endpoints")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    if args.profile:
        list_client_vpn_endpoints(args.profile)
    else:
        list_client_vpn_endpoints(None)

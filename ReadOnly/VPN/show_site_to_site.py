import argparse
import boto3
from datetime import datetime
from dateutil.tz import tzutc

def list_vpn_connections(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2_client = session.client('ec2')

    response = ec2_client.describe_vpn_connections()
    # print(response)

    for vpn_connection in response['VpnConnections']:
        print(f"VPN Connection ID: {vpn_connection['VpnConnectionId']}")
        print(f"Customer Gateway ID: {vpn_connection['CustomerGatewayId']}")
        print(f"Virtual Private Gateway ID: {vpn_connection['VpnGatewayId']}")
        print(f"State: {vpn_connection['State']}")
        print(f"Type: {vpn_connection['Type']}")
            
        print(f"Local Network CIDR: {vpn_connection['Options']['LocalIpv4NetworkCidr']}")
        print(f"Remote Network CIDR: {vpn_connection['Options']['RemoteIpv4NetworkCidr']}")

        print("Routes:")
        for route in vpn_connection['Routes']:
            print(f"  - Destination CIDR: {route['DestinationCidrBlock']} (state: {route['State']})")
        
        for telemetry in vpn_connection['VgwTelemetry']:
            print(f"Tunnel:")
            print(f"  - Outside IP Address: {telemetry['OutsideIpAddress']}")
            print(f"    Status: {telemetry.get('Status', 'N/A')}")
            print(f"    Accepted Route Count: {telemetry['AcceptedRouteCount']}")
            last_status_change = telemetry['LastStatusChange'].astimezone(tzutc()).strftime('%Y-%m-%d %H:%M:%S %Z')
            print(f"    Last Status Change: {last_status_change}")
            print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List AWS Site-to-Site VPN connections")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    if args.profile:
        list_vpn_connections(args.profile)
    else:
        list_vpn_connections(None)

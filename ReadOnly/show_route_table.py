import argparse
import boto3

def list_routes(route_table_id, aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2 = session.client('ec2')

    try:
        response = ec2.describe_route_tables(RouteTableIds=[route_table_id])

        for route_table in response['RouteTables']:
            print(f"Route Table ID: {route_table['RouteTableId']}")

            for route in route_table['Routes']:
                destination_cidr = route.get('DestinationCidrBlock', 'N/A')
                target = route.get('GatewayId', 'N/A')

                if 'TransitGatewayId' in route:
                    target = route['TransitGatewayId']

                print(f"Destination: {destination_cidr}")
                print(f"Target: {target}")
                print(f"State: {route['State']}")
                print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List routes of a routing table")
    parser.add_argument("--route_table_id", type=str, help="Route Table ID")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_routes(args.route_table_id, args.profile)

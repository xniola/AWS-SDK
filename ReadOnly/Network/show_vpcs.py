import argparse
import boto3

def get_name(tags):
    for tag in tags:
        if tag['Key'] == 'Name':
            return tag['Value']
    return 'N/A'

def list_vpcs(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2 = session.client('ec2')

    response = ec2.describe_vpcs()

    for vpc in response['Vpcs']:
        vpc_id = vpc['VpcId']
        vpc_name = get_name(vpc.get('Tags', []))
        
        print(f"VPC ID: {vpc_id}")
        print(f"VPC Name: {vpc_name}")
        print(f"State: {vpc['State']}")
        print(f"CIDR Block: {vpc['CidrBlock']}")

        # List associated route tables
        route_tables_response = ec2.describe_route_tables(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
        for route_table in route_tables_response['RouteTables']:
            route_table_id = route_table['RouteTableId']
            route_table_name = get_name(route_table.get('Tags', []))
            print(f"Route Table ID: {route_table_id} ({route_table_name})")

        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List VPCs and associated route tables")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_vpcs(args.profile)

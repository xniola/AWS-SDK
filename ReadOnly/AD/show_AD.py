import argparse
import boto3

def list_directories(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ds_client = session.client('ds')

    response = ds_client.describe_directories()
    #print(response)

    for directory in response['DirectoryDescriptions']:
        print(f"Directory Name: {directory['Name']}")
        print(f"Directory ID: {directory['DirectoryId']}")
        print(f"Directory Type: {directory['Type']}")
        print(f"Directory Size: {directory['Size']}")
        print(f"VPC Settings: {directory['VpcSettings']}")
        print(f"Stage: {directory['Stage']}")
        print(f"Status: {directory['StageLastUpdatedDateTime']}")
        print()

if __name__ == "__main":
    parser = argparse.ArgumentParser(description="List AWS Directory Service directories")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    if args.profile:
        list_directories(args.profile)
    else:
        list_directories(None)

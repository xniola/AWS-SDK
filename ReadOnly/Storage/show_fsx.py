import argparse
import boto3

def list_fsx_filesystems(profile_name):
    # Initialize the Boto3 FSx client with the specified profile
    session = boto3.Session(profile_name=profile_name)
    fsx_client = session.client('fsx')

    # List FSx for Windows File Server file systems
    file_systems = fsx_client.describe_file_systems()

    # Print information about each file system
    for fs in file_systems['FileSystems']:
        print(f"File System ID: {fs['FileSystemId']}")
        print(f"File System Type: {fs['FileSystemType']}")
        print(f"Creation Time: {fs['CreationTime']}")
        print(f"Lifecycle: {fs['Lifecycle']}")
        print(f"Storage Capacity (GiB): {fs['StorageCapacity']} GiB")
        print(f"DNS Name: {fs['DNSName']}")
        print(f"Deployment Type: {fs['WindowsConfiguration']['DeploymentType']}")
        print(f"File Server Ip: {fs['WindowsConfiguration']['PreferredFileServerIp']}")
        print()

def main():
    parser = argparse.ArgumentParser(description='List FSx for Windows File Server File Systems')
    parser.add_argument('--profile', help='AWS CLI profile name', required=True)

    args = parser.parse_args()
    list_fsx_filesystems(args.profile)

if __name__ == '__main__':
    main()

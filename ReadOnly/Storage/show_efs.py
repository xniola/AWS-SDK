import argparse
import boto3

def list_efs_filesystems(profile_name):
    # Initialize the Boto3 EFS client with the specified profile
    session = boto3.Session(profile_name=profile_name)
    efs_client = session.client('efs')

    # List EFS file systems
    file_systems = efs_client.describe_file_systems()

    # Print information about each file system
    for fs in file_systems['FileSystems']:
        print(f"File System ID: {fs['FileSystemId']}")
        print(f"Creation Time: {fs['CreationTime']}")
        print(f"LifeCycle State: {fs['LifeCycleState']}")
        print(f"Size (GiB): {fs['SizeInBytes']['Value'] / (1024 ** 3):.2f} GiB")
        print(f"Performance Mode: {fs['PerformanceMode']}")
        print()

def main():
    parser = argparse.ArgumentParser(description='List EFS File Systems')
    parser.add_argument('--profile', help='AWS CLI profile name', required=True)

    args = parser.parse_args()
    list_efs_filesystems(args.profile)

if __name__ == '__main__':
    main()

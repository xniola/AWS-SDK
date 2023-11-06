import argparse
import boto3

def list_objects_in_bucket(bucket_name, aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    s3 = session.client('s3')

    try:
        response = s3.list_objects_v2(Bucket=bucket_name)

        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"Object Key: {obj['Key']}")
                print(f"Size: {obj['Size']} bytes")
                print(f"Last Modified: {obj['LastModified']}")
                print()
        else:
            print(f"No objects found in the bucket.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List objects in an S3 bucket")
    parser.add_argument("--bucket_name", type=str, help="S3 bucket name")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_objects_in_bucket(args.bucket_name, args.profile)

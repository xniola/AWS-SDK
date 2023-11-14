import argparse
import boto3

def list_s3_buckets(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    s3 = session.client('s3')

    try:
        response = s3.list_buckets()

        res = ""
        for bucket in response['Buckets']:
            res += f"Bucket Name: {bucket['Name']}\n"

        return res
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List S3 buckets")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_s3_buckets(args.profile)

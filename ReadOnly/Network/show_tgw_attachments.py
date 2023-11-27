import argparse
import boto3

def list_transit_gateway_attachments(aws_profile):
    session = boto3.Session(profile_name=aws_profile)
    ec2 = session.client('ec2')

    try:
        response = ec2.describe_transit_gateway_attachments()

        for attachment in response['TransitGatewayAttachments']:
            print(f"Transit Gateway ID: {attachment['TransitGatewayId']}")
            print(f"Attachment ID: {attachment['TransitGatewayAttachmentId']}")
            print(f"Resource ID: {attachment.get('ResourceId', 'N/A')}")
            print(f"Resource Type: {attachment.get('ResourceType', 'N/A')}")
            print(f"State: {attachment['State']}")
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="List Transit Gateway attachments")
    parser.add_argument("--profile", type=str, help="AWS profile name")

    args = parser.parse_args()
    list_transit_gateway_attachments(args.profile)

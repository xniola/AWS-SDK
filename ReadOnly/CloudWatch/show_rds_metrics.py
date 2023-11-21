import boto3
from datetime import datetime, timedelta

def get_rds_instance_metrics(profile, db_instance_identifier, metric_name, start_time, end_time):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=profile)

    # Create a Boto3 client for CloudWatch using the session
    cloudwatch_client = session.client('cloudwatch')

    # Get the specified metric data for the RDS instance
    response = cloudwatch_client.get_metric_data(
        MetricDataQueries=[
            {
                'Id': 'm1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': 'AWS/RDS',
                        'MetricName': metric_name,
                        'Dimensions': [
                            {
                                'Name': 'DBInstanceIdentifier',
                                'Value': db_instance_identifier
                            },
                        ]
                    },
                    'Period': 300,  # Adjust the period as needed (in seconds)
                    'Stat': 'Average',  # Other options: Sum, Minimum, Maximum, SampleCount
                },
                'ReturnData': True,
            },
        ],
        StartTime=start_time,
        EndTime=end_time,
    )

    # Display the metric data
    print(f"RDS Instance Identifier: {db_instance_identifier}")
    print(f"Metric Name: {metric_name}")
    print("Metric Data:")

    timestamps = response['MetricDataResults'][0].get('Timestamps', [])
    values = response['MetricDataResults'][0].get('Values', [])

    for timestamp, value in zip(timestamps, values):
        timestamp_str = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        print(f"  {timestamp_str}: {value}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch and display RDS instance metrics")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--db-instance-identifier", type=str, required=True, help="RDS instance identifier")
    parser.add_argument("--metric-name", type=str, required=True, help="Name of the metric to fetch")
    parser.add_argument("--hours", type=int, default=1, help="Number of hours to fetch data for (default: 1)")

    args = parser.parse_args()

    # Calculate start and end times based on the specified number of hours
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(hours=args.hours)

    # Call the function to fetch and display RDS instance metrics
    get_rds_instance_metrics(args.profile, args.db_instance_identifier, args.metric_name, start_time, end_time)

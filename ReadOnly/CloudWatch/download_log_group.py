import boto3
from datetime import datetime, timedelta
from tqdm import tqdm  # Import tqdm for the progress bar

def download_all_logs_from_log_group(log_group_name, output_file, start_date=None):
    """
    Download all logs from a CloudWatch Logs log group.

    Parameters:
    - log_group_name: The name of the CloudWatch Logs log group.
    - output_file: The file to save the downloaded logs.
    - start_date: Optional. Custom start date for log events.
    """

    # Create a CloudWatch Logs client
    cloudwatch_logs = boto3.client('logs')

    # Set the start time based on the provided or default start date
    if start_date:
        start_time = start_date
    else:
        start_time = datetime(datetime.now().year, 1, 1, 0, 0, 0, 0)

    # Convert datetime objects to Unix timestamps in milliseconds
    start_timestamp = int(start_time.timestamp() * 1000)

    # Get the total number of log events for progress bar
    total_events = cloudwatch_logs.describe_log_groups(logGroupNamePrefix=log_group_name)['logGroups'][0]['storedBytes']

    # Open the output file for writing
    with open(output_file, 'w') as file:

        # Paginate through log events and download all logs
        with tqdm(total=total_events, unit='B', unit_scale=True, desc='Downloading logs') as pbar:
            while True:
                # Retrieve log events from the log group
                response = cloudwatch_logs.filter_log_events(
                    logGroupName=log_group_name,
                    startTime=start_timestamp,
                    interleaved=True,  # Set to True for interleaved results from multiple log streams
                )

                # Extract and save log events to the output file
                for event in response['events']:
                    file.write(event['message'] + '\n')
                    pbar.update(len(event['message']))

                # Check if there are more log events to retrieve
                next_token = response.get('nextToken')
                if next_token:
                    response = cloudwatch_logs.filter_log_events(
                        logGroupName=log_group_name,
                        startTime=start_timestamp,
                        interleaved=True,
                        nextToken=next_token
                    )
                else:
                    break

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Download all logs from a CloudWatch Logs log group")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--log-group-name", type=str, required=True, help="Name of the CloudWatch Logs log group")
    parser.add_argument("--output-file", type=str, default="downloaded_logs.txt", help="Output file for downloaded logs")
    parser.add_argument("--start-date", type=str, help="Custom start date for log events in ISO format (e.g., 'AAAA-MM-GG[T00:00:00]')")

    args = parser.parse_args()

    # Parse the provided start date if it exists
    start_date = None
    if args.start_date:
        start_date = datetime.fromisoformat(args.start_date)

    # Call the function to download all logs from the specified log group
    download_all_logs_from_log_group(args.log_group_name, args.output_file, start_date)

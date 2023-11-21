import boto3
import sys
import time
from datetime import datetime, timedelta

def list_executed_lambda_functions(aws_profile, time_period_hours):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for CloudWatch Logs using the session
    logs_client = session.client('logs')

    # Calculate the start time for the query
    start_time = datetime.utcnow() - timedelta(hours=time_period_hours)

    try:
        # List log groups (Lambda function names are typically log group names)
        response = logs_client.describe_log_groups()
        log_groups = [log_group['logGroupName'] for log_group in response['logGroups']]

        # Initialize a flag to track if results have been printed
        results_printed = False

        # Iterate through log groups and query for events
        for log_group in log_groups:
            # Query for log events in the last time_period_hours
            query = f"fields @timestamp, @message | sort @timestamp desc | limit 1"
            response = logs_client.start_query(
                logGroupName=log_group,
                startTime=int((start_time - timedelta(minutes=1)).timestamp()) * 1000,  # Convert to milliseconds
                endTime=int(datetime.utcnow().timestamp()) * 1000,  # Convert to milliseconds
                queryString=query,
                limit=1
            )

            # Get the query ID
            query_id = response['queryId']

            # Get query results
            query_status = None
            animation_chars = ["|", "/", "-", "\\"]
            animation_index = 0
            while query_status == 'Running' or query_status is None:
                sys.stdout.write(f"\rWaiting for query to complete ... {animation_chars[animation_index]}")
                sys.stdout.flush()  # Flush stdout
                #time.sleep(0.1)  # Add a small delay for the animation effect
                animation_index = (animation_index + 1) % len(animation_chars)

                response = logs_client.get_query_results(
                    queryId=query_id
                )
                query_status = response.get('status')

            # Clear the line after query completion
            sys.stdout.write("\r" + " " * 50 + "\r")
            sys.stdout.flush()

            # Process the query results
            results = response.get('results', [])
            if results:
                for result in results:
                    for field in result:
                        if field['field'] == '@timestamp':
                            timestamp_str = field['value']
                            execution_time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S.%f")
                            if execution_time > start_time:
                                print(f"Lambda Function (Log Group): {log_group}")
                                print(f"Last Execution Time: {execution_time}")
                                print()
                                results_printed = True
                            break

        # Print a newline character if results were printed
        if results_printed:
            print()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="List Lambda Functions Executed in the Last N Hours")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--time-period", type=int, default=12, help="Time period in hours (default: 12)")

    args = parser.parse_args()
    list_executed_lambda_functions(args.profile, args.time_period)

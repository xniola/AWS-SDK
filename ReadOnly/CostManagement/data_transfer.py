import boto3
import datetime

def generate_data_transfer_cost_report(aws_profile, start_date, end_date, output_filename,granularity):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for the AWS Cost Explorer API using the session
    ce = session.client('ce')

    try:
        # Set default start and end dates to the current month
        if not start_date or not end_date:
            today = datetime.datetime.now()
            start_date = today.replace(day=1)
            next_month = today.replace(month=today.month+1, day=1)
            end_date = next_month - datetime.timedelta(days=1)

        # Define the time period for the report
        time_period = {
            "Start": start_date.strftime("%Y-%m-%d"),
            "End": end_date.strftime("%Y-%m-%d")
        }

        # Define the metrics to include in the report
        metrics = ["UsageQuantity", "BlendedCost"]

        # Define the filter for data transfer costs
        filter = {
            "Dimensions": {
                "Key": "RECORD_TYPE",
                "Values": ["DataTransfer"]
            }
        }

        # Generate the cost and usage report
        response = ce.get_cost_and_usage(
            TimePeriod=time_period,
            Granularity=granularity,
            Metrics=metrics,
            Filter=filter
        )

        with open(output_filename, "w") as report_file:
            for item in response['ResultsByTime']:
                report_file.write(f"Start date: {item['TimePeriod']['Start']}\n")
                report_file.write(f"End date: {item['TimePeriod']['End']}\n")
                report_file.write(f"Data Transfer Usage Quantity: {item['Total']['UsageQuantity']['Amount']} {item['Total']['UsageQuantity']['Unit']}\n")
                report_file.write(f"Blended Data Transfer Cost: {item['Total']['BlendedCost']['Amount']} {item['Total']['BlendedCost']['Unit']}\n")
                report_file.write("\n")

        print(f"Data transfer cost report saved to '{output_filename}'")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Data Transfer Cost Report")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--start-date", type=str, default=None, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", type=str, default=None, help="End date (YYYY-MM-DD)")
    parser.add_argument("--output-filename", type=str, default="./data_transfer_cost_report.txt", help="Output filename")
    parser.add_argument("--granularity",type=str,default="MONTHLY",help="Granularity of the analysis [DAILY/MONTHLY]")

    args = parser.parse_args()

    # Convert provided start and end dates to datetime objects
    start_date = datetime.datetime.strptime(args.start_date, "%Y-%m-%d") if args.start_date else None
    end_date = datetime.datetime.strptime(args.end_date, "%Y-%m-%d") if args.end_date else None

    generate_data_transfer_cost_report(args.profile, start_date, end_date, args.output_filename,args.granularity)

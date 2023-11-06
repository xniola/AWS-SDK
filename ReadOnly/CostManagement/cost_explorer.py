import boto3
import datetime

def generate_monthly_cost_report(aws_profile, start_date, end_date, granularity, output_filename):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Create a Boto3 client for the AWS Cost Explorer API using the session
    ce = session.client('ce')

    try:
        # Define the time period for the report
        time_period = {
            "Start": start_date.strftime("%Y-%m-01"),
            "End": end_date.strftime("%Y-%m-%d")
        }

        # Define the granularity for the report (DAILY, MONTHLY, etc.)
        granularity = granularity.upper()

        # Define the metrics to include in the report
        metrics = ["UnblendedCost"]  # You can include more metrics as needed

        # Generate the cost and usage report
        response = ce.get_cost_and_usage(
            TimePeriod=time_period,
            Granularity=granularity,
            Metrics=metrics
        )
        
        if granularity == "MONTHLY":
            
            with open(output_filename, "w") as report_file:
                report_file.write(f"Start date: {response['ResultsByTime'][0]['TimePeriod']['Start']}\n")
                report_file.write(f"End date: {response['ResultsByTime'][0]['TimePeriod']['End']}\n")
                report_file.write(f"Amount: {response['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']}\n")
                report_file.write(f"Unit: {response['ResultsByTime'][0]['Total']['UnblendedCost']['Unit']}\n")
                report_file.write(f"Amount: {response['ResultsByTime'][0]['Estimated']}\n")
        
        elif granularity == "DAILY":
            for item in response['ResultsByTime']:
                with open(output_filename, "a") as report_file:
                    report_file.write(f"Start date: {item['TimePeriod']['Start']}\n")
                    report_file.write(f"End date: {item['TimePeriod']['End']}\n")
                    report_file.write(f"Amount: {item['Total']['UnblendedCost']['Amount']}\n")
                    report_file.write(f"Unit: {item['Total']['UnblendedCost']['Unit']}\n")
                    report_file.write(f"Estimated: {item['Estimated']}\n")
                    report_file.write("\n")
                                         
        
        print(f"Monthly cost report saved to '{output_filename}'")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate Cost Report per Month or Day")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--start-date", type=str, required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", type=str, required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--granularity", type=str, default="MONTHLY", help="Granularity (e.g., DAILY, MONTHLY)")
    parser.add_argument("--output-filename", type=str, default="./cost_report.json", help="Output filename")

    args = parser.parse_args()

    start_date = datetime.datetime.strptime(args.start_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(args.end_date, "%Y-%m-%d")

    generate_monthly_cost_report(args.profile, start_date, end_date, args.granularity, args.output_filename)

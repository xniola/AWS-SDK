import argparse
import boto3

def get_most_expensive_services(profile_name, start_date, end_date, output_file, granularity,n_services):
    session = boto3.Session(profile_name=profile_name)
    ce = session.client('ce')

    result = ce.get_cost_and_usage(
        TimePeriod={
            'Start': start_date,
            'End': end_date
        },
        Granularity=granularity,  # Use the specified granularity
        Metrics=['UnblendedCost'],
        GroupBy=[
            {
                'Type': 'DIMENSION',
                'Key': 'SERVICE'
            }
        ]
    )

    services = sorted(result['ResultsByTime'][0]['Groups'], key=lambda x: -float(x['Metrics']['UnblendedCost']['Amount']))

    n = n_services 

    with open(output_file, 'w') as file:
        for i, service in enumerate(services[:n], start=1):
            service_name = service['Keys'][0]
            cost = service['Metrics']['UnblendedCost']['Amount']
            result_line = f"{i}. {service_name}: ${cost}\n"
            file.write(result_line)
            print(result_line, end='')

def main():
    parser = argparse.ArgumentParser(description='Show the Most Expensive Services per Month or Day')
    parser.add_argument('--profile', help='AWS CLI profile name', required=True)
    parser.add_argument('--start-date', help='Start date in YYYY-MM-DD format', required=True)
    parser.add_argument('--end-date', help='End date in YYYY-MM-DD format', required=True)
    parser.add_argument('--granularity', help='Granularity for the AWS Cost Explorer query', default='MONTHLY')
    parser.add_argument('--output-file', help='Output file for results', required=True)
    parser.add_argument('--n', help='The number of services to be displayed',default=15, required=False)
    
    args = parser.parse_args()
    get_most_expensive_services(args.profile, args.start_date, args.end_date, args.output_file, args.granularity,int(args.n))

if __name__ == '__main__':
    main()

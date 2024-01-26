import boto3
import pymssql

def execute_sql_commands_on_rds(aws_profile, rds_endpoint, username, password, database, sql_commands):
    # Create a Boto3 session with the specified profile
    session = boto3.Session(profile_name=aws_profile)

    # Connect to RDS
    conn = pymssql.connect(server=rds_endpoint, user='admin', password='<$EH}wP}9lQ<')

    try:
        with conn.cursor() as cursor:
            # Execute each SQL command
            for sql_command in sql_commands:
                cursor.execute(sql_command)
        conn.commit()
        print("SQL commands executed successfully on RDS.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Execute SQL Commands on RDS Instance")
    parser.add_argument("--profile", type=str, required=True, help="AWS CLI profile name")
    parser.add_argument("--rds-endpoint", type=str, required=True, help="RDS instance endpoint")
    parser.add_argument("--username", type=str, required=True, help="RDS instance username")
    parser.add_argument("--password", type=str, required=True, help="RDS instance password")
    parser.add_argument("--database", type=str, required=True, help="RDS database name")
    parser.add_argument("--sql-commands", nargs='+', required=True, help="List of SQL commands to execute")

    args = parser.parse_args()

    execute_sql_commands_on_rds(
        aws_profile=args.profile,
        rds_endpoint=args.rds_endpoint,
        username=args.username,
        password=args.password,
        database=args.database,
        sql_commands=args.sql_commands
    )

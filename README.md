# AWS-SDK

<img src="https://allcode.com/wp-content/uploads/2021/02/Group-169-3.png" alt="alt text"/>


A collection of Python-SDK scripts for automating the most common tasks in AWS

All the scripts were placed in one of the following folders based on the type of operations performed.

### ReadOnly folder
In **ReadOnly** folder you will find all the scripts that can be executed without any particular precautions, since there are read-only operations.
Just make sure to have the proper permissions in your account to execute the specified actions. 
### Operations folder
In **Operations** folder there are some scripts that you should run with caution as they may cause changes to your aws infrastructure  

## Prerequisites
- Install [aws-cli](https://aws.amazon.com/it/cli/)
- Configure your aws profile with ```aws configure sso```
- Install python boto3 library with ```pip install boto3```
   
## Syntax
You can execute the scripts with the following syntax:
```
python3 <script_name.py> --profile <aws_profile_name>
```
Some scripts require additional arguments like the id of the specific resource to be fetched and more.

## Help
Using the option -h or --help, you can see further informations about the script and all the required arguments:
```
python3 <script_name.py> -h
```

## Json output
The default output format is raw text, but it is possible to view the output in json format using the script **txt_to_json.py** provided in this repo:
```
python3 </path/to/script.py> --profile <aws_profile_name> | python3 txt_to_json.py
```

### Example

Default output:
```
$ python3 ReadOnly/Lambda/show_lambdas.py --profile REDACTED
Function Name: Hello-World
Runtime: python3.9
Last Modified: 2023-06-29T09:12:32.558+0000
Handler: instance_scheduler.main.lambda_handler
Role: arn:aws:iam::123456789:role/InstanceScheduler-SchedulerRole-1EIU75QVQP8HD

Function Name: MyFunction
Runtime: python3.11
Last Modified: 2023-09-29T07:17:50.000+0000
Handler: lambda_function.lambda_handler
Role: arn:aws:iam::123456789:role/rdsLambda
```


Json output:

```
$ python3 ReadOnly/Lambda/show_lambdas.py --profile REDACTED | python3 txt_to_json.py
[
  {
    "Function Name": "Hello-World",
    "Runtime": "python3.9",
    "Last Modified": "2023-06-29T09:12:32.558+0000",
    "Handler": "instance_scheduler.main.lambda_handler",
    "Role": "arn:aws:iam::123456789:role/InstanceScheduler-SchedulerRole-1EIU75QVQP8HD"
  },
  {
    "Function Name": "myFunction",
    "Runtime": "python3.11",
    "Last Modified": "2023-09-29T07:17:50.000+0000",
    "Handler": "lambda_function.lambda_handler",
    "Role": "arn:aws:iam::123456789:role/rdsLambda"
  }
]
```

Query Json ouput with jq:

```
$ python3 ReadOnly/Lambda/show_lambdas.py --profile emerald-uat | python3 txt_to_json.py | jq '.[] | select(.["Function Name"] == "myFunction")'
{
    "Function Name": "myFunction",
    "Runtime": "python3.11",
    "Last Modified": "2023-09-29T07:17:50.000+0000",
    "Handler": "lambda_function.lambda_handler",
    "Role": "arn:aws:iam::123456789:role/rdsLambda"
}
```

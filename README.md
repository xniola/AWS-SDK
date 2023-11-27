# AWS-SDK

<img src="https://allcode.com/wp-content/uploads/2021/02/Group-169-3.png" alt="alt text"/>


A collection of Python-SDK scripts for automating the most common tasks in AWS

All the scripts were placed in one of the following folders based on the type of operations performed.

### ReadOnly folder
In **ReadOnly** folder you will find all the scripts that can be executed without any particular precautions, since there are read-only operations.
Just make sure to have the proper permissions in your account to execute the specified actions. 
### Operations folder
In **Operations** folder there are some scripts that you should run with caution as they may cause changes to your aws infrastructure  

## Syntax
Generally, you can execute the scripts following this syntax:
```
python3 <script_name.py> --profile <aws_profile_name>
```

However, some scripts require additional arguments like the id of the specific resource to be fetched and more.

## Help
Using the option -h or --help, you can see all the required arguments for each script:
```
python3 <script_name.py> -h
```

## Json output
The default output format is raw text, but it is possible to view the output in json format using **txt_to_json.py**:
```
python3 </path/to/script.py> --profile <aws_profile_name> | python3 txt_to_json.py
```

The output in json format can be useful and lets you parse and query results with specific tools such as jq

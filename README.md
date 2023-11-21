# AWS-SDK

A collection of Python-SDK scripts for automating the most common tasks in AWS

## ReadOnly folder
In **ReadOnly** folder you will find all the scripts that can be executed without any particular precautions, since there are read-only operations.
Just make sure to have the proper permissions in your account to execute the specified actions. 

## Operations folder
In **Operations** folder there are some scripts that you should run with caution as they may cause changes to your aws infrastructure  

## Syntax
Generally, you can execute the scripts following this syntax:
```
python3 <script_name.py> --profile <aws_profile_name>
```

Some scripts require additional arguments like the id of the specific resource to be fetched.

## Help
Using the option -h or --help, you can see all the required arguments for each script:
```
python3 <script_name.py> -h
```

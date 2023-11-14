import tkinter as tk
from tkinter import messagebox
import subprocess
from modules.show_buckets import list_s3_buckets

def show_custom_messagebox(title, message, width, height):
    custom_messagebox = tk.Toplevel()
    custom_messagebox.title(title)
    custom_messagebox.geometry(f"{width}x{height}")

    label = tk.Label(custom_messagebox, text=message, padx=10, pady=10)
    label.pack()

    ok_button = tk.Button(custom_messagebox, text="OK", command=custom_messagebox.destroy)
    ok_button.pack(pady=10)

def execute_aws_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        output = result.stdout
        if result.returncode == 0:
            show_custom_messagebox("Success", f"Command executed successfully:\n\n{output}",400,200)
        else:
            show_custom_messagebox("Error", f"Command execution failed:\n\n{output}",400,200)
    except Exception as e:
        show_custom_messagebox("Error", f"An error occurred:\n\n{str(e)}",400,200)

def aws_ec2_command(profile):
    # Replace this with your AWS EC2 CLI command
    aws_command = f"aws ec2 describe-instances --profile {profile}"
    execute_aws_command(aws_command)

def aws_s3_command(profile):
    try:
        result = list_s3_buckets(profile)
        output = result
        if result != "":
            show_custom_messagebox("Success", f"Command executed successfully:\n\n{output}",600,300)
        else:
            show_custom_messagebox("Error", f"Command execution failed:\n\n{output}",600,300)
    except Exception as e:
        show_custom_messagebox("Error", f"An error occurred:\n\n{str(e)}",600,300)


# Function to get the selected profile from the dropdown menu
def get_selected_profile():
    return profile_var.get()

# Create the main application window
app = tk.Tk()
app.title("AWS CLI Command Executor")

# Set the window size to a larger dimension (width x height)
app.geometry("800x600")


# Create a label and an entry widget for the AWS profile
profile_label = tk.Label(app, text="AWS Profile:")
profile_label.pack(pady=5)
profile_var = tk.StringVar()
profile_entry = tk.Entry(app, textvariable=profile_var)
profile_entry.pack(pady=10)

# Create buttons
s3_button = tk.Button(app, text="List S3 Buckets", command=lambda: aws_s3_command(get_selected_profile()))
ec2_button = tk.Button(app, text="List EC2 Instances", command=lambda: aws_ec2_command(get_selected_profile()))

# Arrange buttons on the window
s3_button.pack(pady=10)
ec2_button.pack(pady=10)

# Start the GUI event loop
app.mainloop()

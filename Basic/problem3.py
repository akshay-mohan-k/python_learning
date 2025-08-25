import os

# Specify the directory path (current directory in this case)
directory_path = "/"

# List all files and directories in the specified directory
contents = os.listdir(directory_path)
for item in contents:
    print(item)
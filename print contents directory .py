import os

# Specify the directory you want to list
directory = 'D:\\'  # Replace with your directory path

# Get the list of files and directories in the specified directory
entries = os.listdir(directory)

# Print each entry
for entry in entries:
    print(entry)

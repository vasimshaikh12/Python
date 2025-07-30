# Write a Python program to copy the contents of a file to another file.

def copy_file(source_file, destination_file):
    """
    Copy contents from source_file to destination_file.
    If destination_file doesn't exist, it will be created.
    If it exists, it will be overwritten.
    """
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Successfully copied contents from '{source_file}' to '{destination_file}'")
        return True
    except FileNotFoundError:
        print(f"Error: The source file '{source_file}' was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:
# copy_file('source.txt', 'destination.txt')
# 
# # To create a backup copy:
# import os
# from datetime import datetime
# 
# def create_backup(filename):
#     if not os.path.exists(filename):
#         print(f"Error: The file '{filename}' does not exist.")
#         return False
#         
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     backup_file = f"{filename}.bak_{timestamp}"
#     return copy_file(filename, backup_file)
# 
# create_backup('important.txt')

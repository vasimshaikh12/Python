# Write a Python program to read a file line by line and store it into a variable

def file_to_variable(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return ""
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""

# Example usage:
# file_content = file_to_variable('sample.txt')
# print("File content:")
# print(file_content)

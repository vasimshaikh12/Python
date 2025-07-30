# Write a Python program to read a file line by line and store it into a list

def file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Remove newline characters from each line
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Example usage:
# lines = file_to_list('sample.txt')
# print("File content as list:", lines)

# Write a Python program to count the number of lines in a text file.

def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            return sum(1 for _ in file)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return -1
    except Exception as e:
        print(f"An error occurred: {e}")
        return -1

# Example usage:
# line_count = count_lines('sample.txt')
# if line_count >= 0:
#     print(f"Number of lines in the file: {line_count}")

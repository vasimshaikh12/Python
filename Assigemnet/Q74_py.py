# Write a Python program to read first n lines of a file.

def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            for i in range(n):
                line = file.readline()
                if not line:
                    break
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# read_first_n_lines('sample.txt', 5)

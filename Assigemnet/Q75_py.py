# Write a Python program to read last n lines of a file.

def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            # Read all lines and get the last n lines
            lines = file.readlines()
            last_lines = lines[-n:] if len(lines) >= n else lines
            
            for line in last_lines:
                print(line, end='')
                
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# read_last_n_lines('sample.txt', 3)

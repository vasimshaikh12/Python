# Write a Python program to append text to a file and display the text.

def append_to_file(filename, text):
    try:
        # Append text to file
        with open(filename, 'a') as file:
            file.write(text + '\n')
        
        # Read and display the file content
        with open(filename, 'r') as file:
            print("File content after appending:")
            print(file.read())
            
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
append_to_file('sample.txt', 'This is some new text.')

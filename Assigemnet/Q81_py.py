# Write a Python program to write a list to a file.

def write_list_to_file(filename, items, mode='w'):
    """
    Write a list to a file.
    
    Args:
        filename (str): Name of the file to write to
        items (list): List of items to write
        mode (str): File mode - 'w' for write (overwrite), 'a' for append
    """
    try:
        with open(filename, mode) as file:
            for item in items:
                file.write(f"{item}\n")
        print(f"Successfully wrote {len(items)} items to {filename}")
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:
# fruits = ['apple', 'banana', 'cherry', 'date']
# write_list_to_file('fruits.txt', fruits)
# 
# # To append to an existing file:
# more_fruits = ['elderberry', 'fig', 'grape']
# write_list_to_file('fruits.txt', more_fruits, 'a')

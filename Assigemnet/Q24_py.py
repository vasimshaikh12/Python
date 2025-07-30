# Write a Python function to insert a string in the middle of a string.

def insert_middle(original, to_insert):
    middle_index = len(original) // 2
    return original[:middle_index] + to_insert + original[middle_index:]

print(insert_middle("HelloWorld", "Python"))  

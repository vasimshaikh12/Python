# Write a Python script to check if a given key already exists in a dictionary.

my_dict = {'apple': 10, 'banana': 5, 'cherry': 15}
key_to_check = "apple"

if key_to_check in my_dict:
    print(f"Key '{key_to_check}' exists in the dictionary.")
else:
    print(f"Key '{key_to_check}' does not exist in the dictionary.")

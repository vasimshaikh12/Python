# Write a Python function that takes a list and returns a new list withunique elements of the first list.
def unique_elements(lst):
    return list(set(lst))

# Example:
my_list = [1, 2, 2, 3, 4, 4, 5]
print("my list: ",my_list)
print("Unique_list",unique_elements(my_list))  

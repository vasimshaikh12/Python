# Write a Python program to get unique values from a list

def unique_value(x):
    return list(set(x))

value = [9,2,2,3,4,3,5,6,8,7,1,9,5]

print(unique_value(value))
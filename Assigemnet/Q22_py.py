# Write a Python function to reverse a string if its length is a multiple of of 4.

def reverse_if_multiple_of_4(s):
    if len(s) % 4 == 0:
        return s[::-1]
    else:
        return s


print(reverse_if_multiple_of_4("Python")) 
print(reverse_if_multiple_of_4("Abcd"))
print(reverse_if_multiple_of_4("Vasim"))

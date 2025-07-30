# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.

string = input("Enter a string: ")
dict = {}
for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print(dict)




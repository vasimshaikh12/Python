# Write a Python program to add 'in' at the end of a given string (length should be at least 3). If the given string already ends with 'Ing' then add 'lee' instead if the string length of the given string is less than 3, leave it unchanged.

text = input("Enter a string: ")

if len(text) < 3:
    result = text
elif text.lower().endswith("ing"):
    result = text + "lee"
else:
    result = text + "in"

print("Result:", result)

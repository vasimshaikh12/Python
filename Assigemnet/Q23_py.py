# Write a Python program to get a string made of the first 2 and the last 2 characters from a given string. 
# If the string length is less than 2, return the empty string.
def first_last_2_chars(s):
    if len(s) < 2:
        return ''
    return s[:2] + s[-2:]

print(first_last_2_chars("spring")) 
print(first_last_2_chars("a"))       
print(first_last_2_chars("ab"))      

# Write a Python function that checks whether a passed string is palindrome or not


def check_palindrome(s):
    return s==s[::-1]

print(check_palindrome("madam"))
print(check_palindrome("python"))
print(check_palindrome("racecar"))
print(check_palindrome("hello"))


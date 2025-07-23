# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

check_values = lambda a, b: a == b or (a + b) == 5 or abs(a - b) == 5

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Result:", check_values(num1, num2))

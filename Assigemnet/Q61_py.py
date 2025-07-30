# Write a Python function to calculate the factorial of a number (anonnegative integer)


num = int(input("Enter a number : "))

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(f"number of {num} is factorial {factorial(num)}")
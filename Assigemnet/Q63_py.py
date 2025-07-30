# Write a Python function to check whether a number is perfect or not.

def perfect_number(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

print(perfect_number(6))
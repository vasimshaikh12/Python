# Write a Python function to check whether a number is in a given range

def check_range(n):
    if n in range(1,100):
        print(f"Number {n} is in the 'range'")
    else:
        print(f"Number {n} is not in the range")

check_range(1)  
# Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

# Python program to sum three integers, with a condition

for i in range(1,2):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    if a == b or b == c or a == c:
        print("Two values are equal. Sum = 0")
    else:
        total = a + b + c
        print(f"Sum = {a} + {b} + {c} = {total}")

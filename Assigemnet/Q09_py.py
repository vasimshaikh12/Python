# Swapping using a temp variable

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before Swap: a = {a}, b = {b}")

temp = a
a = b
b = temp

print(f"After Swap: a = {a}, b = {b}")

#---------------------------------------------------

# Swapping without using a temp variable

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"Before Swap: a = {a}, b = {b}")

a, b = b, a

print(f"After Swap: a = {a}, b = {b}")

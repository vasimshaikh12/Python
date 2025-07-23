# Q.Write a Python program to find whether a given number is even or odd, and print out an appropriate message to the user.

# Method : 1

number=int(input("Enter a Number : "))

if number % 2 == 0 :
    print(f"This {number} number is even.")
else:
    print(f"This {number} number is odd.")

#---------------------------------------------------

#Method : 2

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(f"The number {number} is {check_even_odd(number)}.")

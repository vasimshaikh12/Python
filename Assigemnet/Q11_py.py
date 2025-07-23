# # write a Python program to check whether a given letter is a vowel or not.

# letter = input("enter a Letter : ")

# if letter in "aeiouAEIOU" :
#     print(f"this {letter} is vowel.")
# else:
#     print(f"this {letter} is not-vowel.")


# Using a function

def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
print(f"The number {number} is {check_even_odd(number)}.")

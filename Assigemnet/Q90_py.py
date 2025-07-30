# Write python program that user to enter only odd numbers, else will raise an exception.

try:
    number = int(input("Enter an odd number: "))
    if number % 2 == 0:
        raise ValueError("Only odd numbers are allowed!")
    print("Thank you! You entered an odd number:", number)
except ValueError as e:
    print("Error:", e)


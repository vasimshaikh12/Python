number=int(input("Enter a Number : "))

if number < 0:
    print("Factorial does not exist for negative numbers.")
elif number ==0 or number ==1:
    print("factorial is 1")
else:
    fact = 1
    for i in range(2,number+1):
        fact *= i
    print(f"Factorial {number} is {fact}")
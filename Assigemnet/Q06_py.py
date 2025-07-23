number = int(input("Enter the number : "))

a=0
b=1
if number <= 0:
    print("Please Enter a Positive Number.")
elif number == 1:
    print("Fibonacci Series:",a)
else:
    print("Fibonacci Series:",end=" ")
    print(a,b,end=" ")
    for i in range(2,number):
        c=a+b
        print(c,end=" ")
        a = b
        b = c
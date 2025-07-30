# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

num_dict = {i: i**2 for i in range(1, 16)}
print(num_dict)

# List where the keys are numbers between 1 and 15.
num_list = [ (i,i*i )for i in range(1,16)]
print(num_list)
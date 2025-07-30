# Write a Python program to remove duplicates from a list.

list = [1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(unique_list)

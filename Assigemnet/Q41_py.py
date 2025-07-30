# Write a Python program to check whether a list contains a sub list

list = [1,2,3,4,5,6,7,8,9,10]

sub_list = [1,2,3]

sub_len=len(sub_list)
found = False

for i in range(len(list)-sub_len+1):
    if list[i:i + sub_len] == sub_list:
        found = True
        break

if found:
    print("Yes, list contain sub_list")
else:
    print("No, List not contain sub_list")
#Write a Python program to unzip a list of tuples into individual lists.

list_of_tuples = [(1,2,3),(4,5,6),(7,8,9)]

l1,l2,l3 =zip(*list_of_tuples)
l1=list(l1)
l2=list(l2)
l3=list(l3)
print(l1)
print(l2)
print(l3)

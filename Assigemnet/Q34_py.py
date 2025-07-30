#  Write a Python function that takes two lists and returns true if they have at least one common member.

l1=[1,2,3,4,5]
l2=[1,5,6,7,8,9]

for i in l1:
    if i in l2:
        print("true")
        break
    else:
        print("false")
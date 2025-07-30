# Write a Python program to find the second smallest number in a list.

def second_smallest(num):
    unique_sorted = sorted(set(num))
    if len(unique_sorted) >= 2:
        print(num)
        print(unique_sorted)
        return unique_sorted[1]
    else :
        return None

num = [1,2,3,4,56,7,6,78,9,8,9,7,8,41,23,6,54,78,9,10]

print(second_smallest(num))
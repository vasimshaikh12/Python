# Write a Python function to get the largest number, smallest Number and sum of all from a list.
def analyze_numbers(num_list):
    if not num_list:
        return "The list is empty."

    largest = max(num_list)
    smallest = min(num_list)
    total = sum(num_list)

    return largest, smallest, total


numbers = [1,2,34,56,7,8,99,100]
largest, smallest, total = analyze_numbers(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum of all numbers:", total)

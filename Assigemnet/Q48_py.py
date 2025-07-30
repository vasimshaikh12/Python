# Write a Python script to sort (ascending and descending) a dictionary by value.

my_dict = {'apple': 10, 'banana': 5, 'cherry': 15,'orange': 20,"mango": 12}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending by value:", asc_sorted)
print("Descending by value:", desc_sorted)

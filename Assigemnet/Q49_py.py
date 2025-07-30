
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5,'f':6}

merged_dict = {**dict1, **dict2, **dict3}
print("Merged Dictionary:", merged_dict)

merged_dict_alt = {}
for d in (dict1, dict2, dict3):
    merged_dict_alt.update(d)

print("Merged Dictionary (using update):", merged_dict_alt)

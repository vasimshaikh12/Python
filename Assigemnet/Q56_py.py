# Write a Python program to map two lists into a dictionary Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).

key = ["a","b","d","c"]
value = [400,400,400,300]
# key = ["apple","banana","orange","kiwi"]
# value = [10,20,30,40]

merge_dict = dict(zip(key,value))

print(merge_dict)
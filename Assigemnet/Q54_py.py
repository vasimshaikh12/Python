# Write a Python program to check multiple keys exists in a dictionary

def key_exist(d,keys):
    return all (key in d for key in keys)


dict = {"a":1,"b":2,"c":3,"d":4}
key_to_check = ["a","c"]

print(key_exist(dict,key_to_check))


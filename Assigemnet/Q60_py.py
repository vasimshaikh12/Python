#Sample string:
#  'w3resource' Expected output:
# • {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}


string = "w3resource"
dict = {}
for char in string:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1

print(dict)
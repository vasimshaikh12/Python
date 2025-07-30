# # Write a Python program to count the number of strings where the string  length is 2 or more and the first and last character are same from a given list of strings.

def count_matching_strings(words):
    count = 0
    matching = []
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count += 1
            matching.append(word)
    
    print("Original list:", words)
    print("Matching strings (length ≥ 2 and same first & last character):", matching)
    print("Count of matching strings:", count)

string_list = ['abc', 'xyz', 'aba', '1221', 'aa', 'b','123','www','121','qwq']
count_matching_strings(string_list)

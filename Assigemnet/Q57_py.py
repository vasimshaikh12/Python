# Write a Python program to find the highest 3 values in a dictionary

dict = {"a":200,"b":100,"c":300,"d":400,"e":500,"f":1253}
print(dict.values())
high_3_values = sorted(dict.values(),reverse = True)
print("sorted values: ",high_3_values)
print("highest 3 values: ",high_3_values[:3])
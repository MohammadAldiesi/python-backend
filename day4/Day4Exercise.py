data = [10, 40, 32, 67, 23, 67, 89, 89]
unique_data = list(set(data))
unique_data.sort()
second_largest = unique_data[-2]
print("Second largest number:", second_largest)

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print("Merged dictionary:", merged)

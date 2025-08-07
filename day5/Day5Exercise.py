dict1 = {'a': 3, 'b': 6, 'c': 1}
dict2 = {'b': 3, 'c': 5, 'd': 2}

merged_dict = {}

for key in dict1.keys() | dict2.keys():
    if (v1 := dict1.get(key)) is not None and (v2 := dict2.get(key)) is not None:
        merged_dict[key] = v1 + v2
    else:
        merged_dict[key] = v1 if v1 is not None else dict2.get(key)

print("Merged dictionary:", merged_dict)

data = [10, 40, 32, 67, 23, 67, 89, 89]
unique_data = list(set(data))

def second_largest(x):
    if len(x) < 2:
        return None

    first, second = x[0], x[1]
    if first < second:
        first, second = second, first

    for n in x[2:]:
        if n > first:
            first, second = n, first
        elif n > second and n != first:
            second = n
    return second

print("Second largest number:", second_largest(unique_data))

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print("Merged dictionary:", merged)

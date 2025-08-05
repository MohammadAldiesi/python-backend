numbers = [12, 45, 7, 34, 89, 21]
sorted_numbers = sorted(numbers)
filtered = [n for n in numbers if n > 30]
squared = [n**2 for n in numbers]
person = ("Mohammad", 24, "Jordan")
name = person[0]
age = person[1]
country = person[2]

print("sorted_numbers:", sorted_numbers)
print("filtered:", filtered)
print("squared:", squared)
print("name:", name)
print("age:", age)
print("country:", country)

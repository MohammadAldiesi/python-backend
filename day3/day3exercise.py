import math
import statistics

data = [10, 20, 30, 40, 50]

mean_value = statistics.mean(data)
std_dev = statistics.stdev(data)
square_roots = [math.sqrt(x) for x in data]

print("Data:", data)
print("Mean:", mean_value)
print("Standard Deviation:", std_dev)
print("Square Roots:", square_roots)


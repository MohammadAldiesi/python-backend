import day3HandsOn
import math
import statistics
import random
import os
import sys

day3HandsOn.add(5, 7)
day3HandsOn.multiply(4, 6)
day3HandsOn.use_math_module()
day3HandsOn.use_random_module()
day3HandsOn.use_os_sys_modules()
print("Add:", day3HandsOn.add(5, 7))
print("Multiply:", day3HandsOn.multiply(4, 6))
print("Square root of 16:", day3HandsOn.math.sqrt(16))
print("Cosine of 0:", day3HandsOn.math.cos(0))
print("Random number (0-100):", day3HandsOn.random.randint(0, 100))
print("Current Working Directory:", day3HandsOn.os.getcwd())
print("Python Executable Path:", day3HandsOn.sys.executable)
data = [10, 20, 30, 40, 50]
print("Data:", data)
print("Mean:", statistics.mean(data))
print("Standard Deviation:", statistics.stdev(data))
print("Square Roots:", [math.sqrt(x) for x in data])

print("----------------------------------------------------------")
import day3exercise

data = [10, 20, 30, 40, 50]
mean_value = day3exercise.statistics.mean(data)
std_dev = day3exercise.statistics.stdev(data)   


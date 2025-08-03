import math
import random
import os
import sys

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def use_math_module():
    print("Square root of 16:", math.sqrt(16))
    print("Cosine of 0:", math.cos(0))

def use_random_module():
    print("Random number (0-100):", random.randint(0, 100))

def use_os_sys_modules():
    print("Current Working Directory:", os.getcwd())
    print("Python Executable Path:", sys.executable)

print("Add:", add(5, 7))
print("Multiply:", multiply(4, 6))
use_math_module()
use_random_module()
use_os_sys_modules()

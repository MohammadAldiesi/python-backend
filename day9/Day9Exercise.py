def multiplier(base):
    def inner(x):
        if base == 0:
            return x * x
        return base * x
    return inner

doubler = multiplier(2)
tripler = multiplier(3)
squarer = multiplier(0)

with open("log.txt", "a") as file:
    file.write(f"Doubler(5) = {doubler(5)}\n")
    file.write(f"Tripler(4) = {tripler(4)}\n")
    file.write(f"Squarer(6) = {squarer(6)}\n")


def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        with open("log.txt", "a") as file:
            file.write(f"{func.__name__} called {wrapper.count} times\n")
        return result
    wrapper.count = 0
    return wrapper

@call_counter
def greet(name):
    return f"Hello, {name}"

greet("Ali")
greet("Sara")


def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                with open("log.txt", "a") as file:
                    file.write(f"Invalid argument in {func.__name__}: {args}\n")
                raise ValueError("Arguments must be positive numbers")
        result = func(*args, **kwargs)
        with open("log.txt", "a") as file:
            file.write(f"{func.__name__}({args}) = {result}\n")
        return result
    return wrapper

@validate_positive
def add(a, b):
    return a + b

add(3, 5)
add(10, 20)

def validate_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError("Arguments must be positive numbers")
        return func(*args, **kwargs)
    return wrapper

@validate_positive
def add(a, b):
    return a + b

print(add(3, 5))
print(add(10, 20))
print(add(-3, 5))  # Raises ValueError

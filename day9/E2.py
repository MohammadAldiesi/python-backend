def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@call_counter
def greet(name):
    return f"Hello, {name}"

print(greet("mOhammad"))
print(greet("Naser"))
print("Function called:", greet.count, "times")

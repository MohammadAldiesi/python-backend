class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

def simple_generator(n):
    for i in range(n):
        yield i * i

numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
squared_dict = {x: x**2 for x in numbers}
unique_squares = {x**2 for x in numbers}

countdown = CountDown(5)
for num in countdown:
    print(num)

for val in simple_generator(5):
    print(val)

print(squared)
print(squared_dict)
print(unique_squares)


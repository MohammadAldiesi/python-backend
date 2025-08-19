# Exercise 1
print("Exercise 1")
class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        else:
            self.a, self.b = self.b, self.a + self.b
            self.count += 1
            return self.b

fib = Fibonacci(10)
for num in fib:
    print(num)

# Exercise 2
print("\nExercise 2")
def alternating_signs(numbers):
    sign = 1
    for num in numbers:
        yield num * sign
        sign *= -1

nums = [1, 2, 3, 4, 5]
for val in alternating_signs(nums):
    print(val)

# Exercise 3
print("\nExercise 3")
words = ["hello", "world"]
ascii_dict = {word: {ch: ord(ch) for ch in word} for word in words}
print(ascii_dict)

# Exercise 4
print("\nExercise 4")
text = "Programming is fun"
vowels = {ch.upper() for ch in text if ch.lower() in "aeiou"}
print(vowels)

# Exercise 5
print("\nExercise 5")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

prime_gen = primes()
for _ in range(6):
    print(next(prime_gen))

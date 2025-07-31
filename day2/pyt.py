def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def factorial(n):
    factorial = 1

    if n < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        print("The factorial of", n, "is", factorial)



print(fibonacci_series(15))
print(factorial(10))


def multiplier(base):
    def inner(x):
        if base == 0:
            return x * x
        return base * x
    return inner

doubler = multiplier(2)
tripler = multiplier(3)
squarer = multiplier(0)

print(doubler(5))
print(tripler(4))
print(squarer(6))

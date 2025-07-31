num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number.")
else:
    prime = True
    i = 2
    while i < num:
        if num % i == 0:
            prime = False
            break
        i += 1
    if prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")

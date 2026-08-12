def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not possible for negative numbers")

else:
    result = factorial(n)

    print("Factorial =", result)

from functools import reduce

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
factorial_lambda = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)
num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial using recursion:", factorial_recursive(num))
    print("Factorial using lambda & reduce:", factorial_lambda(num))
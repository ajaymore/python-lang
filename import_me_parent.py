__author__ = 'Mystique'

# functions


def fib(n):
    a, b, result = 1, 2, []
    while a < n:
        print(a, end=' ')
        result.append(a)
        a, b = b, a + b
    print()  # Empty line
    return result
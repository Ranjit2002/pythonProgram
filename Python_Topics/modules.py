def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def exp(a, b):
    return a ** b


def flo_div(a, b):
    return a // b


def factorial(n):
    if n == 1:
        return 1
    c = 1
    for i in range(1, n+1):
        c *= i
    return c


def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a)
        a, b = b, a + b



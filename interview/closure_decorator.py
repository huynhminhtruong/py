# First class function
# Properties of first class functions:
    # - A function is an instance of the Object type.
    # - You can store the function in a variable.
    # - You can pass the function as a parameter to another function.
    # - You can return the function from a function.
    # - You can store them in data structures such as hash tables, lists

import logging
import functools as ft
logging.basicConfig(filename="output.log", level=logging.INFO)

def square(n):
    return n * n

def mapping(func, a):
    n = len(a)
    for i in range(n):
        a[i] = func(a[i])
    return a

def sum_numbers(*args):
    a = args # receive params as a tuples
    print(a)

def add(*args):
    return sum(args)

def product(*args) -> int:
    return ft.reduce(lambda x, y: x * y, args)

def sub(*args) -> int:
    return ft.reduce(lambda x, y: x - y, args)

def div(*args) -> int:
    return ft.reduce(lambda x, y: x // y, args)

def logger(func):
    def wrapper(*args):
        logging.info("Running function {0} with args: {1}".format(func.__name__, args))
        print(func(*args))
    return wrapper

@logger
def factor(*args) -> int:
    return ft.reduce(lambda x, y: x * y, args, 1)

if __name__ == "__main__":
    # n = int(input())
    # a = mapping(square, [int(i) for i in input().split()]) # custom mapping
    # sum_numbers(*a) # pass params as a tuples
    add_n = logger(add)
    product_n = logger(product)
    sub_n = logger(sub)
    div_n = logger(div)

    add_n(1, 2)
    product_n(1, 2)
    sub_n(1, 2)
    div_n(10, 2)
    factor(1, 2, 3)
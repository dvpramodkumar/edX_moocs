# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 13:06:06 2016

@author: ericgrimson
"""

# Fibonacii using Recursion


def recursive_fibonacii(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return recursive_fibonacii(x-1) + recursive_fibonacii(x-2)


print(recursive_fibonacii(20))
print(recursive_fibonacii(30))


# Fibonacii using Iteration


def iterative_fibonacii(n):
    a = 0
    b = 1

    i = 0
    while i < n:
        c = a + b
        a = b
        b = c
        i += 1
    return c


print(iterative_fibonacii(20))
print(iterative_fibonacii(30))
print(iterative_fibonacii(40))

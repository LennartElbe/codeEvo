import functools
import typing
import string
import random
import pytest

def divisors(x: int):
    """This function recieves a positive Integer n and returns a list of its divisors
       Examples:
       A poitive Integer d is a divisor from n, if n divided by d has no rest.
       divisors(10) == [1, 2, 5, 10]
       divisors(23) == [1, 23]
       divisors(3) == [1, 3] 
       """
    result = []
    for i in range(1, x + 1):
        if not(x % i):
            print(i)
            result.append(i)
    return result

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
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
######################################################################
## Lösung Teil 2. (Tests)
def test_5():
    assert divisors(10) == [1, 2, 5, 10]
def test_6():
    assert divisors(23) == [1, 23]
def test_7():
    assert divisors(3) == [1, 3] 
######################################################################

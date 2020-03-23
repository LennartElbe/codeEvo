import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int):
    """Calculates all divisors of n with rest zero
    
    Args:
        n(int): An positive integer n > 0
    
    Return:
        a list of all divisors of n"""
    if n > 0:
        lst = []
        for i in range(1, n + 1):       # without zero, else Error
            if n % i == 0:
                lst += [i]
        return lst
    else:
        return "Error, n hast to be > 0"
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert(divisors(6) == [1,2,3,6])
    assert(divisors(20) == [1,2,4,5,10, 20])
    assert(divisors(0) == "Error, n has to be > 0")
    assert(divisors(-20) == "Error, n has to be > 0")
    assert(divisors(7) == [1, 7])                   # prime
######################################################################

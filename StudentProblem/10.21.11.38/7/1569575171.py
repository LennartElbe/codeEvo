import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """this function checks whether d is a Teiler of n
    Args: n a positive natural number
    returns: a list of all the Teilers with no repetitions"""
    res = []
    for d in range(1,n + 1):
        if n % d == 0:
            res.append(d)
    return res
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(4) == [1,2,4]
    assert divisors(3) == [1,3]
    assert divisors(1) == [1]
######################################################################

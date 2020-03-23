import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """Function to give all divisors of a given number"""
    assert n > 0 "n needs to be a positive whole number!"
    res = []
    for i in range(1,n+1):
        if n % i == 0:
            res += [i]
    return res
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(4) == [1,2,4]
    assert divisors(5) == [1,5]
    assert divisors(0) == Exception
######################################################################

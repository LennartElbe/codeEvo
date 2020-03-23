import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """Returns a list with all dividors from n.
    Arguments:
        n: A positive Integer
    """
    res = []
    for x in range(1, n+1):  # Or range((1, (n+1) // 2) + 1)
        if n % x == 0:
            res += [x]
    return res
    
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(0) == []
    assert divisors(10) == [1, 2, 5, 10]
    assert divisors(23) == [1, 23]
######################################################################

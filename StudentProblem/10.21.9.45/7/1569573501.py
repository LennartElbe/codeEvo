import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """
    Creates a list containing all divisors of a given integer and returns the list.
    n: A given integer
    """
    res = []
    if n == 0:
        res = res + n
        return res
    elif n < 0:
        return "Number not within defined parameters."
    else:
        for d in range(n + 1):
            if n/d == 0:
                res = res + d
        return res
######################################################################
## Lösung Teil 2. (Tests)
def div_test(n):
    assert divisors(0) == [0]
    assert divisors(1) == [1]
    assert divisors(4) == [1, 2, 4]
    assert divisors(5) == [1, 5]
######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """Returns a list of all divisors(without a rest) of a given number.
    Args:
        n: an integer
    Returns:
        res: a list of all the divisors.
    """
    res = []
    for x in range(n):
        if n%x == 0:
            if x not in res:
                res.append(x)
            else:
                break
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(20) == [1, 2, 4, 5, 10]
######################################################################

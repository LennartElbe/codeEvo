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
    res = [1]
    if n <= 0:
        return("The input must be an integer greater than 0.")
    if n == 1:
        return 1
    for x in range(2, n):
        if n%x == 0:
            if x not in res:
                res.append(x)
            else:
                break
    return res
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(20) == [1, 2, 4, 5, 10]
    assert divisors(7) == [1, 7]
    assert divisors(1) == [1]
    assert divisors(0) == "The input must be an integer greater than 0."

######################################################################

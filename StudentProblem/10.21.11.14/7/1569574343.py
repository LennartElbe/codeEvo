import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """Function to return every divisor of n
    
    Args:
        n: an integer
    
    Returns:
        List of every divisor of n
    """
    res = []
    for d in range(1, n+1):
        if n % d == 0:
            res += [d]
    return res
######################################################################
## Lösung Teil 2. (Tests)
def test_norm():
    assert divisors(10) == [1, 2, 5, 10]

def test_one():
    assert divisors(1) == [1]


######################################################################

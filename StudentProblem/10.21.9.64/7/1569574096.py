import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """the function give the divisor numbers of n
    
    Args:
    n(int): natural Number
    
    Returns:
    return a list with the divisor number of n
    """
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result += [i]
    return result
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    """test of the function divisor"""
    assert(divisors(10)) == [1, 2, 5, 10] 
######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """Calculates all the divisors of a given number, without rest.
    Args:
        A natural number n.
    Returns:
        A list of all divisors of n, without rest.
    """
    result = []
    for d in range(1, n + 1):
        if n % d == 0:
            result = result + [d]
    return result
        
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    divisors(5) == [1, 5]
    divisors(12) == [1, 2, 3, 4, 6, 12]
    divisors(8) == [1, 2, 4, 8]
######################################################################

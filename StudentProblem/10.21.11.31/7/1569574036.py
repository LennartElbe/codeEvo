import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """Calculates all the divisors of a given number.
    Args:
        A natural number n.
    Returns:
        A list of all divisors of n.
    """
    result = []
    for d in range(1, n + 1):
        if n % d == 0:
            result = result + [d]
    return result
        

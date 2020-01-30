import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """Function to return every divisor of n
    
    Args:
        n: an integer
    
    Returns:
        List of every divisor of n
    """
    res = []
    d = 1
    while d <= n:
        if n % d == 0:
            res += [d]
            d += 1
    print(res)
    return res

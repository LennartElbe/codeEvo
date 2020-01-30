import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """Compute a list of divisors for a given input
    
    Args:
        n(int): A given number
    
    Returns:
        res(list): list of numbers that are divisors of n
    """
    res = []
    for d in range(1, 10+1):
        if d % n == 0:
            res.append(d)
    return res

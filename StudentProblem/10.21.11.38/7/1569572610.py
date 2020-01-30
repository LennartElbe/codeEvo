import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """this function checks whether d is a Teiler of n
    Args: n a positive natural number
    returns: a list of all the Teilers with no repetitions"""
    res = []
    for d in range(0,n + 1):
        if n % d == 0:
            res.append(d)
    return res

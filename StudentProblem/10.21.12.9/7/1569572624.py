import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """Returns a list with all dividors from n.
    Arguments:
        n: A positive Integer
    """
    res = []
    for x in range(1, n+1):
        if n % x == 0:
            res += [x]
    return res
    

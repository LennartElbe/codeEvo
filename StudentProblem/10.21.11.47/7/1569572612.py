import functools
import typing
import string
import random
import pytest

def divisors(n:int) -> list:
    """
    Returns a list of all divisors of n.
    
    Args:
    n:int the number to be used.
    
    Returns:
    divisors a list of divisors of n.
    """
    divisors = []
    for d in range(1, n + 1):
        if n % d == 0:
            divisors.insert(d)
    return divisors

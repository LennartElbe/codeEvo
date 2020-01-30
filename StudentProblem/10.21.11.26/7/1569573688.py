import functools
import typing
import string
import random
import pytest

def divisors(n: int):
    """Calculates all divisors of n with rest zero
    
    Args:
        n(int): An positive integer n > 0
    
    Return:
        a list of all divisors of n"""
    if n > 0:
        lst = []
        for i in range(1, n + 1):       # without zero, else Error
            if n % i == 0:
                lst += [i]
        return lst
    else:
        return "Error, n hast to be > 0"

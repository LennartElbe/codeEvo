import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """Function to give all divisors of a given number"""
    res = []
    for i in range(1,n+1):
        if n % i == 0:
            res += [i]
    return res

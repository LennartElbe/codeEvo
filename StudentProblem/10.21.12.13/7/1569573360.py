import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """Function to give all divisors of a given number
    args: n: int number which is checked of its divisors
    returns: divisors(4) == [1,2,4]
    """
    res = []
    for i in range(1,n+1):
        if n % i == 0:
            res += [i]
    return res

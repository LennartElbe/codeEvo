import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """Returns a list of all divisors(without a rest) of a given number.
    Args:
        n: an integer
    Returns:
        res: a list of all the divisors.
    """
    res = [1]
    if n <= 0:
        return("A divisor must be greater than 0.")
    if n == 1:
        return 1
    for x in range(2, n):
        if n%x == 0:
            if x not in res:
                res.append(x)
            else:
                break
    return res

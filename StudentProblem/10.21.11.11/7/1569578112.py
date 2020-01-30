import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """
    Args:
        n: an integer
    Returns:
        a list of all divisors of n
     """
    div_list = []
    if n < 0:
        print("positivity please!")
    else:
        for d in range(1, n+1):
            if n % d == 0:
                div_list += [d]
    return div_list

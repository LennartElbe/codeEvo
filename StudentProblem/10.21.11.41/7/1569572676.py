import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """returns a list of all divisors of an positive integer without any repetitions.
       If the number n is not positive, 'False' is returned."""
    if n < 1:
        return False
    res = []
    for i in range(1, n+1):
        if n%i == 0:
            if i in res:
                break
            else:
                res += [i]
    return res

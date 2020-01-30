import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    res = []
    if n < 0:
        return "n must be greater than 0"
    for d in range(2, n):
        if n // d == 0:
            res += [d]
    return res

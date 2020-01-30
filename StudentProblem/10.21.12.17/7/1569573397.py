import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    res = []
    for i in range(n):
        if n % (i + 1) == 0:
            res += [i + 1]
    return res

print(divisors(100))

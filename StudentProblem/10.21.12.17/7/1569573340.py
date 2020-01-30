import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    res = []
    for i in range(n):
        if n % (i + 1) == 0:
            res += i
    return res

print(divisors(10))

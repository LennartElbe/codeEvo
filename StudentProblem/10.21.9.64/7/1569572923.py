import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result += [i]
    return result

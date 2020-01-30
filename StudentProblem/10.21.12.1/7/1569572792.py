import functools
import typing
import string
import random
import pytest

def divisors(x: int):
    result = []
    for i in range(x + 1):
        if not(x % i):
            reasult.append(i)
    return result

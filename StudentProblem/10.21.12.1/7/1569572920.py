import functools
import typing
import string
import random
import pytest

def divisors(x: int):
    result = []
    for i in range(1, x + 1):
        if not(x % i):
            print(i)
            result.append(i)
    return result

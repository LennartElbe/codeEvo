import functools
import typing
import string
import random
import pytest

def divisors(x:int) -> list:
    result = []
    for i in range(1, x):
        if x % i == 0:
            result = result + [i]
    return result

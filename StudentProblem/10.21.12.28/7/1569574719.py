import functools
import typing
import string
import random
import pytest

def divisors(n :int) -> list:
    ls = []
    count = 2
    while n != 0:
        if n % count == 0:
            ls.append(n)
            n = n // count
            count = 2
        else:
            count += 1
    return ls
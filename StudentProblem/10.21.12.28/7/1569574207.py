import functools
import typing
import string
import random
import pytest

def divisors(n :int) -> list:
    ls = []
    count = 1
    while n % count == 0 and n != 0:
        ls.append(n)
        n = n // count
        count += 1
    else:
        count += 1
    return ls

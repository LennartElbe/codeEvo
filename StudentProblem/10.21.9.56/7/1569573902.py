import functools
import typing
import string
import random
import pytest

def divisors(n: int):
    res = []
    d = int(input())
    if d not in res and d % n == 0:
        res += [d]
    return res        

import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    teiler = []
    for i, k in list(range(n+1)):
        if i % k == 0:
            teiler.append(i)
    return teiler
        

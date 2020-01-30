import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    start_lst = [range(n+1)]
    teiler = []
    for i, k in start_lst:
        if i % k == 0:
            teiler.append(k)
    return teiler
        

import functools
import typing
import string
import random
import pytest

def divisors(n:int)-> list:
    res = []
    if n == 1:
        return [n]
    else:     
        for d in range(1,n):
            if n%d == 0:
                res.append(d)
    return res

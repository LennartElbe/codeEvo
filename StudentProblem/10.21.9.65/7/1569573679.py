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
        for d in range(1,n+1):
            check = (n%d == 0)
            if check:
                res.append(d)
    return res

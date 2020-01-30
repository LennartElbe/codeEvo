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
        for i in range(n):
            if i%n == 0:
                res += [i]
    return res

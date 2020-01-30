import functools
import typing
import string
import random
import pytest

def list_filter(x:int, xs:list):
    res = []
    n = len(xs)
    for i in range(n):
        if xs[i] <= x:
            res += [xs[i]]
    return res

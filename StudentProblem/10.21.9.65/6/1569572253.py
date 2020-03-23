import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x:int, xs:list):
    res = []
    n = len(xs)
    for i in range(n):
        if xs[i] <= x:
            res += [xs[i]]
    return res
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(0, []) == []
    assert list_filter(5, [6, 7, 8, 9]) == []
    assert list_filter(5, [0, 2, 4, 6, 8, 10]) == [0, 2, 4]
    assert list_filter(5, [5, 6, 7, 8, 9]) == [5]
######################################################################

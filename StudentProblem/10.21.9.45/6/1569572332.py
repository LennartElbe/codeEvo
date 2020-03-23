import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """
    Filters a list for elements smaller than a given integer and returns the resulting list.
    x: An integer number
    xs: A given list
    """
    res = []
    for a in xs:
        if x >= a:
            res = res + a
    return res
        
######################################################################
# Lösung Teil 2. (Test)

def filter_test(x, xs):
    assert list_filter(2, [1, 2, 3]) == [1, 2]
    assert list_filter(0, [1, 2, 3]) == []
    assert list_filter(3, []) == []
    assert list_filter(15, [1, 2, 3]) == [1, 2, 3]
######################################################################

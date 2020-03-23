import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """finds all elements in xs, which are smaller or equal compared to x"""
    res = []
    for i in xs:
        if i > x:
            break
        else:
            res += [i]
    return res
######################################################################
# Lösung Teil 2. (Test)

def list_filter_test():
    assert(list_filter(3, [1, 2, 3, 4])) == [1, 2, 3]
    assert(list_filter(2, [])) == []
    assert(list_filter(1, [2, 3, 4])) == []
######################################################################

import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Returns a list with all numbers from xs, which are smaller or equal x.
    Arguments:
        x: A positive Integer
        xs: A list with integers
    """
    res = []
    for number in xs:
        if number <= x:
            res += [number]
    return res
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(5, []) == []
    assert list_filter(0, [1, 2, 3]) == []
    assert list_filter(10, [2, 4, 6]) == [2, 4, 6]
    assert list_filter(5, [2, 5, 8]) == [2, 5]
######################################################################

import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """this function returns all elements in the list smaller or same as x
    args: x, a natural number and xs, a list
    returns: list of elements in the list xs that are smaller or the same as x"""
    res = []
    for i in xs:
        if i <= x:
            res.append(i)
    return res        
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    """this fucntion tests list_filter"""
    assert list_filter(3, [1,3,5]) == [1, 3]
    assert list_filter(3, [3, 6, 8]) == [3]
    assert list_filter(5, [7,9,8]) == []
######################################################################

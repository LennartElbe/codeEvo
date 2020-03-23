import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Function to return list of elements from xs, which are smaller than or equal to x
    
    Args:
        x: an integer
        xs: a list
    Returns:
        a list which contains every element out of xs, smaller than or equal to x
    """
    res = []
    for i in xs:
        if i <= x:
            res += [i]
    return res
######################################################################
# Lösung Teil 2. (Test)

def test_empty():
    assert list_filter(5, []) == []
    
def test_mixed():
    assert list_filter(5, [1, 5, 10]) == [1, 5]
    
def test_oneel():
    assert list_filter(5, [10]) == []
    
######################################################################

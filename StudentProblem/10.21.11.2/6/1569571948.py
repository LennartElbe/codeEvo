import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """ Function returns list of all elements from xs smaller than x.
    Args:   x: int, 
            xs: list
    
    """
    l= []
    for i in xs: #looping
        if xs[i] >= i:
            l  += [xs[i]]
    return l
######################################################################
# Lösung Teil 2. (Test)

def test_filter():
    assert list_filter(2,[1,2,3]) == [2,3]
    assert list_filter(2,[0]) == []
    assert list_filter(2,[3,2,3]) == [3,2,3]
######################################################################

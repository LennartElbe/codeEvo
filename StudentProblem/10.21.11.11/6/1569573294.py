import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Args:
        x: an integer
        xs: a list of integers
        
       Returns:
        a list of integers lesser or equal than x
    """
    res = []
    for n in xs:
        if n <= x:
            res += [n]
    return res
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(0, []) == []
    assert list_filter(1, [0,1,2]) == [0,1]
    assert list_filter(-1,[-2,1]) == [-2]
    assert list_filter(5,[i for i in range(0,100)]) == [k for k in range(0,6)]
######################################################################

import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x, xs):
    """
    """
    result = []
    for element in xs:
        if element <= x:
            result.append(element)
    return result
######################################################################
# Lösung Teil 2. (Test)

def test1():
    a = []
    b = [1,2,3,4,5,6,7]
    c = [0, 2]
    d = [0.2, 0.5, 4.3]
    assert list_filter(a, 20) == [0]
    assert list_filter(b, -1) == []
    assert list_filter(c, 2) == [0, 2]
    assert list_filter(d, 4.3) == [4.3]
######################################################################

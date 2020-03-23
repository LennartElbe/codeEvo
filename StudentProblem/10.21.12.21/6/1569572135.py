import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """alle elemente <= x als liste zurück geben"""
    res =[]
    for i in xs:
        if i <= x:
            res.append(i)
        else:
            continue
    return res

list_filter(0, [5, 15, 37, 1, 0])
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(5, [1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5]
    assert list_filter(0, [1, 2, 3, 4, 5, 6, 7]) == []
    assert list_filter(0, []) == []
    assert list_filter(7, []) == []
    #assert list_filter(0, [5, 15, 37, 1, 0]) == [5, 15, 37, 1, 0]
######################################################################

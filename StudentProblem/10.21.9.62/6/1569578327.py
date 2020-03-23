import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list):
    """gibt die Liste aller Elemente aus xs zurück, die kleiner oder gleich x sind.
    Args: 
    x: ist eine Zahl
    xs: liste von Zahlen"""
    res = [y for y in xs if y <= x]
    return res
print(list_filter(3, [1,2,3])
def test_list_filter():
    assert list_filter(3, [1, 2, 3]) == [1, 2, 3]
    assert list_filter(0, [1]) == []
######################################################################
# Lösung Teil 2. (Test)

#def test_list_filter():
    #assert 
######################################################################

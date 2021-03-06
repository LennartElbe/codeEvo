import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x, xs):
    """ 
    x: Int
    xs: List
    Diese funktion returnt die werte der liste, welche kleiner als x sind."""
    L = []
    for i in xs:
        if x <= i:
            L.append(i)
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert (list_filter(3, [1,2,3,4,5,6]) == [1,2,3])
    assert (list_filter(-1, [-2, -1, 0, 1]) == [-2, -1])
    assert (list_filter(1, [2,3,4,5] == [])
    assert (list_filter(1, []) == [])
######################################################################

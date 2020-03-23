import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x, xs):
    l = []
    for y in xs:
        if y <= x:
            l += [y]
    return l
######################################################################
# Lösung Teil 2. (Test)

def test_bla():
    assert True

def test_list():
    assert [5] == [6]
    
######################################################################

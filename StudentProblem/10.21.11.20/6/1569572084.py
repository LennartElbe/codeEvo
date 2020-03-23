import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    if xs is None:
        return None
    else:
        for a in xs:
            n = []
            if a <= x:
                n.append(a)
                return n
            else:
                return n
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(5, [1,2,3,4,5,6])== [1,2,3,4,5]
    assert list_filter(6, [])== None
    assert list_filter(1, [2,3,4])== []
    assert list_filter(6, [1,2,3,4,5])==[1,2,3,4,5]
######################################################################

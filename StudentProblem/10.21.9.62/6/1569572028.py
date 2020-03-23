import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list):
    res = [y for y in xs if y <= x]
    return res

def test_list_filter():
    assert list_filter(3, [1, 2, 3]) == [1, 2, 3]
    assert list_filter(0, [1]) == []
######################################################################
# Lösung Teil 2. (Test)


######################################################################

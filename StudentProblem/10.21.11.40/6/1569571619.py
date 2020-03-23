import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    return list(filter(lambda y: y <= x, xs))
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(10, []) == []
    assert list_filter(10, [1, 2, 11]) == [1, 2]
    assert list_filter(10, [200, 400]) == []
######################################################################

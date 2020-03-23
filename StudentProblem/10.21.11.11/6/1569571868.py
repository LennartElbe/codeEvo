import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    res = []
    for n in xs:
        if n <= x:
            res += n
    return res
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    x = 0
    xs = []
    assert list_filter(x, xs) == []
######################################################################

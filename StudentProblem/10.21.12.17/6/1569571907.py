import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    res = []
    for number in xs:
        if number == x:
            res += number
    return res
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(4, [3, 2, 4, 7]) == [3, 2, 4]
######################################################################

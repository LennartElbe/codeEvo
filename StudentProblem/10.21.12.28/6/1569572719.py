import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs:list) -> list:
    ls = []
    for i in xs:
        if x <= i:
            ls.append(i)
    return ls
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(10, [2, 3, 5]) == []
    assert list_filter(8, [2, 4, 7]) == []
    assert list_filter(0, [1, 2, 3]) == [1, 2, 3]
######################################################################

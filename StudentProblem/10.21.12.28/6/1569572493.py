import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs) -> list:
    ls = []
    for i in xs:
        if i <= i:
            ls.append(i)
    return ls
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(5, [1, 2, 3]) == [1, 2, 3]
    assert list_filter(0, [2, 3, 5]) == []
    assert list_filter(8, [2, 4, 7]) == []
######################################################################

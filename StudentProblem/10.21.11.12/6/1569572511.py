import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    filtered_list = []
    i = 1
    while i < len(xs):
        if x <= xs[i]:
            filtered_list.append(xs[i])
            i += 1
        elif x >= xs[i]:
            i += 1
    return filtered_list
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(5, [1,2,4,5,8,9]) == [5, 8, 9]
    assert list_filter(5, []) == []
######################################################################

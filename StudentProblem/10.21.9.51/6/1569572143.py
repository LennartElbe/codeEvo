import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list):
    temp_list = []
    for y in xs:
        if y <= x:
            temp_list.append(y)
    return temp_list
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert(list_filter(5, [1,5])) == [1, 5]
    assert(list_filter(4, [1,5])) == [1]
    assert(list_filter(5, [6,8])) == []
    assert(list_filter(5, [1,2,3,4,5])) == [1,2,3,4,5]
######################################################################

import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list):
    same_or_smaller = []
    for i in xs:
        if i <= x:
            same_or_smaller += i
    return same_or_smaller
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(4, [1,2,3,4,5,6]) == [1,2,3,4]
    assert list_filter(10, [-1, 0 , 10]) == [-1, 0 , 10]
######################################################################

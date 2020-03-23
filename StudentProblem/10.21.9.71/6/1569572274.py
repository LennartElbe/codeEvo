import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x, xs):
    new_list = []
    for i in xs:
        if i <= x:
            new_list = new_list + [i]
    return new_list
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    list1 = [1]
    list2 = [1, 2, 3, 4, 5]
    assert list_filter(1, list1) == [1]
    assert list_filter(5, list2) == [5]
######################################################################

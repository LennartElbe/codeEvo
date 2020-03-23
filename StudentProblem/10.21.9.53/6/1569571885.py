import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    ret_list = []
    for i in xs:
        if i <= x:
            ret_list + i
    return ret_list
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter_a:
    a = 3
    b = [1, 2, 3, 4, 5]
    assert list_filter == [1, 2, 3]
######################################################################

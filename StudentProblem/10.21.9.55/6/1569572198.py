import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    new_list = []
    for i in xs:
        if i <= x:
            new_list.append(i)

######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_fliter(4, [1,2,3,4,5]) = [4,5] 
######################################################################

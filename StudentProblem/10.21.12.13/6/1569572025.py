import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Function to filter a given list to a given Argument
    args: x: int which gives the variable to comparte the list with
          xs: the list which will get filterd
    returns: list_filter(1,[]) == []
    """
    res = []
    if xs == []:
        return []
    else:
        for i in xs:
            if i <= x:
                res += [i]
        return res
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(4,[5,6,1,2]) == [1,2]
    assert list_filter(1,[]) == []
######################################################################

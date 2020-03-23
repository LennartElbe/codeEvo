import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x : int, xs : list) -> list:
    "takes a x integer and a list xs and returns all elements within the xs if it is equal oder smaller"
    li = []
    for i in xs:
        if i <= x:
            li = li + [i]
    return li
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(0,[]) == [] #empty
    assert list_filter(10,[1,2,3,5]) == [1,2,3,5] #all
    assert list_filter(5,[6,7,8]) #none
######################################################################

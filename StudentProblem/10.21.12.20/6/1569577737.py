import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list):
#gibt alle ganzzahligen Zahlen aus der Liste xs aus, die in der Liste und Funktionsparameter xs enthalten sind
    same_or_smaller = []
    for i in xs:
        if i <= x:
            same_or_smaller = [same_or_smaller]+[i]
    return same_or_smaller
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(4, [1,2,3,4,5,6]) == [1, 2, 3, 4]
    assert list_filter(10, [1,1,1, 12]) == [1,1,1]
    assert list_filter(0, [0, 0, -1]) == [0, 0, -1]
######################################################################

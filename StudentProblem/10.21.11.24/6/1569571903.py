import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs. list) -> list:
    """Filtert eine Liste und gibt die Werte kleiner gleich x zurück"""
    returnlist = []
    for i in xs:
        if i =< x:
            returnlist.append(i)
    return returnlist
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    testlist = []
    assert list_filter(0, testlist) == []
######################################################################

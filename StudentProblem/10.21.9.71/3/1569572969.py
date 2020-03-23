import functools
import typing
import string
import random
import pytest

def leap(x):
    if x % 4 == 0:
        return True
    elif (x % 100 == 0) and (not(x % 400 == 0)):
        return True
    print(1700 / 4)
    return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert(leap(2019)) == False
    assert(leap(2004)) == True
    assert(leap(1700)) == True
######################################################################

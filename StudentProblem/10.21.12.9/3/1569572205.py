import functools
import typing
import string
import random
import pytest

def leap(jear: int) -> bool:
    if jear <= 1582:
        return False
    if jear % 4 == 0:
        if jear % 100 == 0 and jear % 400 != 0:
            return False
        else:
            return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1999) == False
    assert leap(2000) == True
    assert leap(1000) == False
######################################################################

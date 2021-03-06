import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    "schaut noch ob das Jahr ein Schaltjahr ist
    Args: year ist eine Zahl"
    if year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False

######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2016) == True
    assert leap(1999) == False
######################################################################

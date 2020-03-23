import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    if year%4 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%400 == 0:
        return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1900) == False
    assert leap(2000) == True
######################################################################

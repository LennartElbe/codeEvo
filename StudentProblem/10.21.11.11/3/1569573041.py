import functools
import typing
import string
import random
import pytest

def leap(year: int) -> str:
    if year < 1583:
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return True

######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1582) == False
    assert leap(1583) == True
######################################################################

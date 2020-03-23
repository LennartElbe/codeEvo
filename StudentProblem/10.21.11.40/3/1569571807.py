import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    assert year > 1582
    return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1600)
    assert not leap(1601)
    assert not leap(1700)
######################################################################

import functools
import typing
import string
import random
import pytest

def leap(year: int) -> str:
    if year < 1583:
        print("oh no")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        print(year,"is leapyear")
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1582) == 'oh no'
######################################################################

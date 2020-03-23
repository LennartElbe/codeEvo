import functools
import typing
import string
import random
import pytest

def leap(x: int) -> str:
    if x > 1582:
        if x%4 == 0:
            if x%100 == 0 and x% 400 != 0:
                return print("x ist kein Schaltjahr")
            else:
                return print("x ist ein Schaltjahr")
        else:
            return print("x ist kein Schaltjahr")
    else:
        return print("x ist kein Schaltjahr")
            
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1400) == "x ist kein Schaltjahr"
    assert leap(2020) == "x ist ein Schaltjahr"
######################################################################

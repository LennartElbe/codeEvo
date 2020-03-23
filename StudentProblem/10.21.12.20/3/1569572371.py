import functools
import typing
import string
import random
import pytest

def leap(year:int) -> bool:
    if year < 1582:
        return "Ungültige Eingabe"
    else:
        if year % 400 != 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
            
######################################################################
## Lösung Teil 2 (Tests)

def test_leap(year):
    assert leap(1580) == "Ungültige Eingabe"
    assert leap(1900) == False
    assert leap(1600) == True
######################################################################

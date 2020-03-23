import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """Tests if a given year is a leapyear.
    Args:
        Year - a given integer > 1582.
    Returns:
        If the year is a normal year or a leapyear.
    """
    if year > 1582:
        if year % 4 == 0:
            return True
        if year % 100 == 0 and year % 400 != 0:
            return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    leap(2000) == True
    leap(1900) == False
    leap(1997) == False
    leap(1996) == True
######################################################################

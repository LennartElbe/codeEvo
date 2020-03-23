import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """checks if year is a leap year and returns 'True' if yes, otherwise function returns 'False'.
       The year to be checked can not be before year 1582.
    """
    if year <= 1582:
        return False
    if year%100 == 0 and year%400 != 0:
        return False
    elif year%4 == 0:
        return True
######################################################################
## Lösung Teil 2 (Tests)

def leap_test():
    assert(leap(1582)) == False
    assert(leap(2020)) == True
    assert(leap(2100)) == False
######################################################################

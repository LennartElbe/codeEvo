import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """
    Checks if a year after 1582 is a leap year and returns True or False.
    year: A given integer
    """
    if year > 1582:
        if year % 4 == 0 and (year % 100 == 0 or year % 400 != 0):
            return True
        else:
            return False
    else:
        print("Get your calender straight")
######################################################################
## Lösung Teil 2 (Tests)

def leap_test(year):
    assert leap(2000) == False
    assert leap(1196) == "Get your calender straight"
    assert leap(1996) == True
######################################################################

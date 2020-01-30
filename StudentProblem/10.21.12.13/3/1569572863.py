import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """Function to check if a given year is a leap year
    args: year: int given year to check
    """
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False

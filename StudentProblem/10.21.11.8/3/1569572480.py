import functools
import typing
import string
import random
import pytest

def leap(x: int):
    """Checks if a given year is a leap year(after 1582).
    Args:
        x: int(a year)
        
    Returns:
        True or False.
    """
    if x < 1582:
        return("The gregorian calendar wasn'n invented yet")
    else:
        if x % 4 == 0:
            return True
        elif x%100 == 0 and x%400 != 0:
            return False
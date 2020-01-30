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

import functools
import typing
import string
import random
import pytest

def leap (x:int)->bool:
    """tests if a year x is a leapyear
        args: a year x
        returns: true if the year x is a leapyear, false otherwise """
    if x < 1582:
        return False
    if x % 4 == 0 and x % 100 != 0:
        return True
    if x % 100 == 0 and x % 400 != 0:
        return False
    else:
        return True

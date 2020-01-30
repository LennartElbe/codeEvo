import functools
import typing
import string
import random
import pytest

def leap (x:int)->bool:
    """tests if a year x is a leapyear
    args: a year x
    returns: true if the year is a leapyear, otherwise false"""
    if x < 1582:
        return False
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
            else:
                return False
    else:
        return False

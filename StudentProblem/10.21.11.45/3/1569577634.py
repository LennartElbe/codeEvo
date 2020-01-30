import functools
import typing
import string
import random
import pytest

def leap(x):
    """return True when the x a leap year and False when it's not """
    if x % 4 == 0 or x % 100 == 0 and x % 400 != 0:
        return True
    else:
        return False

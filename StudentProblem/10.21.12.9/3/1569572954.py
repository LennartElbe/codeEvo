import functools
import typing
import string
import random
import pytest

def leap(jear: int) -> bool:
    """Returns a bool if the given Jear is a 'Schaltjahr'.
    Arguments:
        jear: A positive Integer (jear) greater then 1582.
    """
    if jear <= 1582:
        return False
    if jear % 4 == 0:
        if jear % 100 == 0 and jear % 400 != 0:
            return False
        else:
            return True
    else:
        return False

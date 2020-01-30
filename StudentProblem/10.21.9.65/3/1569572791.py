import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    if year%4 == 0:
        if year%100 == 0 and year%400 != 0:
            return False
        else:
            return True
    """
        return True
    elif year%100 == 0:
        return False
    elif year%400 == 0:
        return True
    else:
        return False
    """

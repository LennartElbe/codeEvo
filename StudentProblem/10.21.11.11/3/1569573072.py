import functools
import typing
import string
import random
import pytest

def leap(year: int) -> str:
    if year < 1583:
        return False
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        return True
    else:
        return False


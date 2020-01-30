import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    assert year > 1582
    return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)

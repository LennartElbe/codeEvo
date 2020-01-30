import functools
import typing
import string
import random
import pytest

def leap(year:int) -> bool:
    if year // 4 == 0 && !(year // 100 == 0):
        return true
    elif year // 100 && !(year // 4 == 0):
        return false
    else:
        return false

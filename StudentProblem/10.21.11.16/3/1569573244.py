import functools
import typing
import string
import random
import pytest

def leap(j: int) -> bool:
    if j % 4 == 0 and (j % 100 == 0 or j % 400 != 0):
        return True
    elif j % 4 == 0 and (j % 100 == 0 and j % 400 != 0):
        return False
    else:
        return False

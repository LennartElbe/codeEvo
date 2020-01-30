import functools
import typing
import string
import random
import pytest

def leap(x: int) -> bool:
    if not(x % 100) and x % 400:
        return False
    elif not(x % 4):
        return True
    else:
        return False

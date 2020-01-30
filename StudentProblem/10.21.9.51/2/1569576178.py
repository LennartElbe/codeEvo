import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int):
    if not n > 0:
        return False
    else:
        x = str(n)
        y = reversed(x)
        if x is y:
            return True
        else:
            return False

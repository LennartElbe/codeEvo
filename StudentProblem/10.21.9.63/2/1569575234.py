import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    if n < 0:
        return "number must be greater than 0!"
    if str(n) == (str(n)[::-1]):
        return True
    else:
        return False

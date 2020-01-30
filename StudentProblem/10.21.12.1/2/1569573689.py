import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

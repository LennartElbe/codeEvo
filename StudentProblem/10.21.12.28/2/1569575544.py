import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    if list(str(n)[::-1] == list(str(n)):
        return True
    else:
        return False

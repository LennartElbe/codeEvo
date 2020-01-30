import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    n_str = str(n)
    if n_str == n_str[-1::-1]:
        return True
    else:
        return False

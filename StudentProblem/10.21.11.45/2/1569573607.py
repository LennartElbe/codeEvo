import functools
import typing
import string
import random
import pytest

def is_palindromic(n):
    if n <= 0:
        pass
    else:
        n = str(n)
        if n == n[-1:]:
            return True
        else:
            return False

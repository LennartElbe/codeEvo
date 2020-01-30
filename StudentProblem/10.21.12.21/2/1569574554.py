import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int):
    if n > 0:
        s = str(n)
        return s[1::1,-1]

print(is_palindromic(1001))

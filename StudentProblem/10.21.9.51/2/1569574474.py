import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    if not n > 0:
        return n
    else:
        
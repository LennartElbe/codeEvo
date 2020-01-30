import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    return True if list(str(n))[::-1] == list(str(n))

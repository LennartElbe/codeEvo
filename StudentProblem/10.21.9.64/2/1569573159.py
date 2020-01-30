import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    result = str(n)
    if result [-1::-1] == str(n):
        return True
    else:
        return False

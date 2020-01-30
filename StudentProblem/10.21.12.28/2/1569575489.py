import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    if [str(n)][::-1] == [str(n)] and n > 0:
        return True
    else:
        return False

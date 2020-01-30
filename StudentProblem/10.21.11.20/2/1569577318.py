import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    n > 0
    if n == 0:
        return None
    else:
        for i in str(n[:len(str(n)):-1]):
            p += i
            if int(p) == int(n):
                return True
            else:
                return False
             

import functools
import typing
import string
import random
import pytest

def is_palindromic(n : int) -> str:
    if n > 0:
        return False
    n = str(n)
    m = n[::-1]
    n = int(n)
    m = int(m)
    if n == m:
        return "Palindrom"
    else:
        return "kein Palindrom"
    

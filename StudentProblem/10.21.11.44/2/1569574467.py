import functools
import typing
import string
import random
import pytest

def is_palindromic(n : int) -> bool:
    if n > 0:
        return False
    n = str(n)
    m = n[::-1]
    if n == m:
        return "Palindrom"
    else:
        return "kein Palindrom"
    

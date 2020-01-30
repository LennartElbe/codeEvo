import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int):
    'if the given number is palindromic number return True or not return False'
    s = str(n)
    if n[:] == n[-1::-1]:
        return True
    else:
        return False
    


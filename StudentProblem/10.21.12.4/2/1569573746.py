import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int):
    if n < 0:
        return False
    number = str(n)
    if number == number[-1::-1]:
        return True
    else:
        return False
    
       

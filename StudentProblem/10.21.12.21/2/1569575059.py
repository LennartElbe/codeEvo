import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int):
    if n > 0:
        s = str(n)
        if s == operator.inv(s):
            return True
        #return s[0:,-1]

print(is_palindromic(1001))


import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int): -> bool
    s = str(n)
    if n[:] == n[-1::-1]:
        return True
    else:
        return False
x = 'lujain'    
print(x[-1::-1])

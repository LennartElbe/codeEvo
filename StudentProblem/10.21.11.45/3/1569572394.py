import functools
import typing
import string
import random
import pytest

def leap(x):
    if x % 4 == 0 or x % 100 == 0 and x % 400 == 0:
        return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test():
    assert leap(2000)
    assert leap(2001)
######################################################################

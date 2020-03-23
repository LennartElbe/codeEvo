import functools
import typing
import string
import random
import pytest

def leap (x:int)->bool:
    if x < 1582:
        return False
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return True
            return False
        return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test():
    assert leap (1500) == False
######################################################################

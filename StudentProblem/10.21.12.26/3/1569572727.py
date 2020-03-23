import functools
import typing
import string
import random
import pytest

def leap (x:int)->bool:
    if x < 1582:
        return 0
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return true
        return false
    return true
    else:
        return false
######################################################################
## Lösung Teil 2 (Tests)

def test():
    assert leap (1500) == false
######################################################################

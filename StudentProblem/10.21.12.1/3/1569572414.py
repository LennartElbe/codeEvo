import functools
import typing
import string
import random
import pytest

def leap(x: int) -> bool:
    if not(x % 100) and x % 400:
        return False
    elif not(x % 4):
        return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_4():
    assert leap(2000) == True
    assert leap(1800) == False
    assert leap(1616) == True
######################################################################

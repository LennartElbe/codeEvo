import functools
import typing
import string
import random
import pytest

def leap(x):
    if x // 100 and not x // 400:
        return False
    elif x // 4:
        return True
######################################################################
## Lösung Teil 2 (Tests)

def test_4():
    assert leap(2000) == True

######################################################################

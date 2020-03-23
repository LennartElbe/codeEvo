import functools
import typing
import string
import random
import pytest

def leap(x: int) -> bool:
    """This function recieves a Year and returns wether
       it is a Schaltjahr or not
       A Schaltjahr is a year where February has 29 days"""
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

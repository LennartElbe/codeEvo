import functools
import typing
import string
import random
import pytest

def leap(year):
    """ 
    Args:
        year: Int
    Diese Funktion ergibt für ein eingegebenes jahr ob es ein Schaltjahr ist oder nicht.
    Return: False
            True"""
    n = year
    if n % 4 == 0:
        if n % 100 == 0:
            return False
        elif n % 400 == 0:
            return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert(leap(2006) == False)
    assert(leap(2007) == True)

######################################################################

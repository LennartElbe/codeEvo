import functools
import typing
import string
import random
import pytest

def schaltjahr(x: int):
    """Gibt an ob sich das eingegebene Jahr um ein Schaltjahr handelt.
    Agrs:
       int: das jahr
      
    Return:
       True wenn es stimmt ansonsten False
    """
    if x // 4 or (x // 100 and not x // 400):
        return True
    else:
        return False

######################################################################
## Lösung Teil 2 (Tests)

def test_schaltjahr():
    assert(schaltjahr(1582)) == True
    assert(schaltjahr(2006)) == True
    assert(schaltjahr(2010)) == False
######################################################################

import functools
import typing
import string
import random
import pytest

def schaltjahr(jahr: int):
    if jahr // 4 or (jahr // 100 and not jahr // 400):
        return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_schaltjahr():
    assert(schaltjahr(1582)) == True
######################################################################

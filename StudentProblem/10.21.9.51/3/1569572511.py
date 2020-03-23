import functools
import typing
import string
import random
import pytest

def schaltjahr(jahr: int):
    if jahr // 4 or (jahr // 100 and not jahr // 400):
        return 0
    else:
        return 1
######################################################################
## Lösung Teil 2 (Tests)

def test_schaltjahr():
    assert(schaltjahr(1582)) == 0
######################################################################

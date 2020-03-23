import functools
import typing
import string
import random
import pytest

def leap(jahrzahl: int) -> bool:
    'return True if the given year is schaltjahr and false if not'
    if jahrzahl > 1582:
        if jahrzahl % 100 == 0 and jahrzahl% 400 != 0:
            return True
        else:
            return False
    else:
        print('jahrzahl ist kleiner als 1582')
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2000) == False
    assert leap(2400) == True
    assert leap(155) == 'jahrzahl ist kleiner als 1582'
######################################################################

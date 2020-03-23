import functools
import typing
import string
import random
import pytest

def leap(year):
    """
    Nimmt eine Jahreszahl als Parameter und prüft ob es sich um ein Schaltjahr handelt.
    Definition Schaltjahr rch vier teilbar ist. Ausnahme: Jahreszahl durch einhundert, aber nicht 
    durch vierhundert teilbar, so handelt es sich doch um ein normales Jahr.
    
    args:
        year: int (positives integer >= 1582)
        
    return:
        evaluation: bool (True, wenn year ein Schaltjahr, False wenn kein Schaltjahr
    """
    if year  % 4 == 0 and year > 1582:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    a = 1604
    b = 2100
    c = 404
    assert leap(a) == True
    assert leap(b) == False
    assert leap(c) == False
######################################################################

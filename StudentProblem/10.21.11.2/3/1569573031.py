import functools
import typing
import string
import random
import pytest

def leap(x:int) -> bool:
    """ Funktion leap nimmt eine Jahreszahl als Parameter 
    und gibt zurück, ob es sich um ein Schaltjahr handelt.
    Args: x(int) die Jahreszahl
    Returns: True or False, ob Schaltjahr
    Notes:
    Seit der Einführung des Gregorianischen Kalenders in 1582 liegt prinzipiell ein Schaltjahr vor, 
    wenn die Jahreszahl durch vier teilbar ist. 
    Ausnahme: ist die Jahreszahl durch einhundert, aber nicht durch vierhundert teilbar, 
    so handelt es sich doch um ein normales Jahr.
    """
    if x > 1582:
        if x%4 == 0:
            if (x%100 == 0 and x%400 != 0):
                return False
            else: 
                return True
        return False
        
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    """ Test function for leap
    """
    assert leap(1581) == False
    assert leap(1600) == True
    assert leap(1800) == False
######################################################################

import functools
import typing
import string
import random
import pytest

def leap(Jahreszahl: int) -> bool:
    """ Funktion, die berechnet, ob eine gegebene Jahreszahl ein Schaltjahr ist.
    
        Args:
            Jahreszahl: ganzzahlige Zahl > 1582
            
        Ergebnis:
            True, wenn Schaltjahr, sonst False
    """
    Schaltjahr = False
    if Jahreszahl % 4 != 0:
        Schaltjahr = False
    elif Jahreszahl % 4 == 0:
        if Jahreszahl % 100 == 0 and Jahreszahl % 400 == 0:
            Schaltjahr = True
        elif Jahreszahl % 4 == 0 and Jahreszahl % 100 != 0 :
            Schaltjahr = True
        else:
            Schaltjahr = False          
    return Schaltjahr

######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1600) == True, "Fall: durch 4, 100 und 400 teilbar"
    assert leap(1604) == True, "Fall: nur durch 4 teilbar"
    assert leap(1603) == False, "Fall: nicht durch 4 teilbar"
    assert leap(1700) == False, "Fall: durch 4 und 100 teilbar, nicht durch 400 teilbar"
######################################################################

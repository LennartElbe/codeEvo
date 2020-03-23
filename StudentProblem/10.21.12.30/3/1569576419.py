import functools
import typing
import string
import random
import pytest

J1 = 1600 # 1600/4=400, 1600/400=4, 1600/100=16 ==> True
J2 = 1604 # nur durch 4 teilbar ==> True
J3 = 1603 # nicht durch 4 teilbar ==> False
J3 = 1700 # durch 4 und 100 teilbar, nicht durch 400 teilbar ==> False

def leap(Jahreszahl: int) -> bool:
    """ Funktion, die berechnet, ob eine gegebene Jahreszahl ein Schaltjahr ist.
    
        Args:
            Jahreszahl: ganzzahlige Zahl > 1582
            
        Ergebnis:
            True, wenn Schaltjahr, sonst False
    """
    Schaltjahr = False
    if Jahreszahl % 4 == 0 or (Jahreszahl % 100 == 0 and Jahreszahl % 400 == 0):
        Schaltjahr = True
    return Schaltjahr

######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1600) == True, "Fall: durch 4, 100 und 400 teilbar"
    assert leap(1604) == True, "Fall: nur durch 4 teilbar"
    assert leap(1603) == False, "Fall: nicht durch 4 teilbar"
    assert leap(1700) == False, "Fall: durch 4 und 100 teilbar, nicht durch 400 teilbar"
######################################################################

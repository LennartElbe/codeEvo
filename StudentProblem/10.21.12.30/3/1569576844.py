import functools
import typing
import string
import random
import pytest

J1 = 1600 # 1600/4=400, 1600/400=4, 1600/100=16 ==> True
J2 = 1604 # nur durch 4 teilbar ==> True
J3 = 1603 # nicht durch 4 teilbar ==> False
J4 = 1700 # durch 4 und 100 teilbar, nicht durch 400 teilbar ==> False
print("J1= 1600:", J1 % 4, J1 % 100, J1 % 400)
print("J2= 1604:", J2 % 4, J2 % 100, J2 % 400)
print("J3= 1603:", J3 % 4, J3 % 100, J3 % 400)
print("J4= 1700:", J4 % 4, J4 % 100, J4 % 400)

def leap(Jahreszahl: int) -> bool:
    """ Funktion, die berechnet, ob eine gegebene Jahreszahl ein Schaltjahr ist.
    
        Args:
            Jahreszahl: ganzzahlige Zahl > 1582
            
        Ergebnis:
            True, wenn Schaltjahr, sonst False
    """
    Schaltjahr = False
    if Jahreszahl % 400 != 0:
        Schaltjahr = False
    elif Jahreszahl % 4 == 0:
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

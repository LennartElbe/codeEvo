import functools
import typing
import string
import random
import pytest

def leap(jz: int):
    """ leap year wenn durch 4 teilbar, ODER durch 100 und 400 teilbar, wenn 100 aber nicht 400 normales jahr
        jz muss >= 1582 sein
       
    """
    if jz >= 1582:
        if jz % 4 == 0:
            #print(jz, "ist ein Schaltjahr")
            return True
        elif jz % 100 == 0:
            if jz % 400 == 0:
                #print(jz, "ist ein Schaltjahr")
                return True
            else:
                #print(jz, "ist KEIN Schaltjahr")
                return False
        else:
            #print(jz, "ist KEIN Schaltjahr")
            return False
    else:
        #print("Falsche Eingabe, keine Jahreszahl!")
        return False

print(leap(2004))
print(leap(2005))
print(leap(1500))

"""
2004 ist ein Schaltjahr
True
2005 ist KEIN Schaltjahr
False
Falsche Eingabe, keine Jahreszahl!
False
"""
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2004) == True
######################################################################

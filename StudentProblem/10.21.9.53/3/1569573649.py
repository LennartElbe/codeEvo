import functools
import typing
import string
import random
import pytest

def leap(year: int) -> str:
    """
        Funktion prüft für die eingegebene Jahreszahl, ob sie ein Schaltjahr ist oder nicht.
        Rückgabewerte:  "Schaltjahr" = Schaltjahr
                        "Kein Schaltjahr" = Kein Schaltjahr
                        False= keine gültige Eingabe
    """
    if year < 1582: # Teste, ob Eingabe gültig
        return False
    elif (year % 4) != 0: # Teste, ob durch 4 teilbar ohne Rest
        return "Kein Schaltjahr"
    elif (year % 100) == 0 and (year % 400) != 0: # Teste, ob durch 100, aber nicht 400 teilbar ohne Rest
        return "Kein Schaltjahr"
    else:
        return "Schaltjahr"
    
        
######################################################################
## Lösung Teil 2 (Tests)

def test_leap_a():
    jahr = 1500
    assert leap(jahr) == False
def test_leap_b():
    jahr = 2011
    assert leap(jahr) == "Kein Schaltjahr"
def test_leap_c():
    jahr = 2000
    assert leap(jahr) == "Schaltjahr"
def test_leap_d():
    jahr = 2004
    assert leap(jahr) == "Schaltjahr"
def test_leap_e():
    jahr = 1700
    assert leap(jahr) == "Kein Schaltjahr"
def test_leap_f():
    jahr = -1
    assert leap(jahr) == False
######################################################################

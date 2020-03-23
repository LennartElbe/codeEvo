import functools
import typing
import string
import random
import pytest

def leap(n: int)->str:
    if n <= 1582:
        return ("Falsche Eingabe")
    else:
        if n%4== 0 and not n%100 == 0:
            return ("Schaltjahr")
        elif n%100 == 0 and n%400 == 0:
            return ("Schaltjahr")
        else:
            return("kein Schaltjahr")
            
######################################################################
## Lösung Teil 2 (Tests)

assert leap(2012) == "Schaltjahr"
assert leap(1) == "Falsche Eingabe"
assert leap(2011) == "kein Schaltjahr"
assert leap(2000) == "Schaltjahr"
assert leap(1900) == "kein Schaltjahr"
######################################################################

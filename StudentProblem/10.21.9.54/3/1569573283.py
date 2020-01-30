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
            

import functools
import typing
import string
import random
import pytest

def leap(year: int) -> Bool:
    """Eine Funktion, die uns mit dem boolwert verrät, 
    ob die eingegeben Jahreszahl ein Schaltjahr ist oder nicht
    """
    x = year
    try:
        if x > 1582:
            print("Diese Jahreszahl behandeln wir nicht.")
        if x % 4 == 0:
            if x % 100 == 0 and x % 400 != 0:
                return False
            else:
                return True

                    
                    
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2018)== False
    assert leap(0) == "Diese Jahreszahl behandeln wir nicht."
    assert leap(1600) == True
######################################################################

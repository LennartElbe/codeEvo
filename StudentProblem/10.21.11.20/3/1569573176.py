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
    assert 1582 < x:
        if x % 4 == 0:
            try:
                if x % 100 == 0 and x % 400 != 0:
                     return False
                else:
                    return True
            except AssertionError:
                print("Diese Jahreszahl behandeln wir nicht.")
                    
                    

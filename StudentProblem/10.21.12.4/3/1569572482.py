import functools
import typing
import string
import random
import pytest

def leap(m: int)->bool:
    """ Die Funktion leap nimmt eine Jahreszahl als Parameter und gibt 
        ob es sich um ein Schaltjahr handelt zurück.
        
        Args: m: Das Jahr zum testen
        
        return:
            Boolean True oder False
            True wenn es ein Schaltjahr ist
            False wenn nicht
    
    """
    if m < 1582:
        return 
    if m % 100 == 0 and m % 400 != 0 and m % 4:
        return False
    else:
        return True

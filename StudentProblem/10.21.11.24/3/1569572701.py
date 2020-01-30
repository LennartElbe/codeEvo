import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """Testet eine Jahreszahl, ob sie ein Schaltjahr ist
    Arg: year
    Return: bool True, wenn Schaltjahr
            None, wenn Eingabe kleiner 1582
    """
    if year < 1582:
        return None
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False
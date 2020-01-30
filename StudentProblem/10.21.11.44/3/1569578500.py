import functools
import typing
import string
import random
import pytest

def leap(n : int) -> bool:
    """takes a year n > 1582 and returns depending on the year either "Schaltjahr" or 
    "kein Schaltjahr" or "False" in case the year is to small. """
    if n >= 1582:
        return "False"
    if n%4 == 0:
        if n%100 == 0 and not n%400 == 0:
            return "kein Schaltjahr"
        return "Schaltjahr"
    else:
        return "kein Schaltjahr"
        
        
import functools
import typing
import string
import random
import pytest

def leap(n : int) -> bool:
    if n => 1582:
        return "False"
    if n % 100 == 0 and not n % 400 == 0:
        return "kein Schaltjahr"
    if n % 4 == 0:
        return "Schaltjahr"
    else:
        return "kein Schaltjahr"
        
        

import functools
import typing
import string
import random
import pytest

def leap(x: int) -> str:
    if x > 1582:
        if x%4 == 0:
            if x%100 == 0 and x% 400 != 0:
                return str(x) + " ist kein Schaltjahr"
            else:
                return str(x) + " x ist ein Schaltjahr"
        else:
            return str(x) + " x ist kein Schaltjahr"
    else:
        return str(x) + "ist kein Schaltjahr"
            

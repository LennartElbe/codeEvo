import functools
import typing
import string
import random
import pytest

def leap (x:int)->bool:
    if x < 1582:
        return false
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                return true
        return false
    return true
######################################################################
## Lösung Teil 2 (Tests)


######################################################################

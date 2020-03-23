import functools
import typing
import string
import random
import pytest

def leap(j: int)-> bool:
    if j%4 == 0:
        if j%100 == 0 and j%400 != 0:
            return False
        else:
            return True
    else:
        return False
     

######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2004) == True 
######################################################################

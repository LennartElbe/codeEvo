import functools
import typing
import string
import random
import pytest

def leap(n:int)->bool:
    if n>1582:
        if n % 4==0:
            return True
        elif n % 400==0:
            return True
        else:
            return False
    else:
        print('please enter a year  >1582')
        


######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2000)==True
    assert leap(1996)==True
    assert leap(1582)=='please enter a year >1582'
######################################################################

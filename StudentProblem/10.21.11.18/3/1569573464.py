import functools
import typing
import string
import random
import pytest

def leap(year) -> int:
    year >= 1582
    if year % 400 == 0:
        return print("False")
    elif year % 100 == 0:
        return print("True")
    elif year % 4 == 0:
        return print("True")
    else:
        print("Kein Schaltjahr")
        
 
######################################################################
## Lösung Teil 2 (Tests)

def test_leap1(year) -> int:
    assert leap(1581)
    
def test_leap2(year) -> int:
    assert leap(1900) 
  """ 
def test_leap3(year) -> int:
    assert(leap) year = 2000
    
def test_leap1(year) -> int:
    assert(leap) year = 1996
    """
######################################################################

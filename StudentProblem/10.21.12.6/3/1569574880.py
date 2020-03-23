import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """Function to test if a given year is a leap year or not.
    
    Args:
        year(int): Given year
        
    Returns:
        True if year is a leap year False if year is not a leap year

    """
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
 
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2018) == False
    assert leap(1600) == True
 
######################################################################

import functools
import typing
import string
import random
import pytest

def leap(n: int) -> bool:
    """Checks if a given year after 1581 is a leap year.
    Args: 
        n (int): a year
        
    Returns:
        bool: Whether the year is a leap year
    """
    if n % 4 == 0:
        if n % 100 == 0:
            if n % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
   
                
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    y1, y2, y3, y4 = 1997, 2004, 1900, 2000
    assert leap(y1) == False
    assert leap(y2) == True
    assert leap(y3) == False
    assert leap(y4) == True
######################################################################

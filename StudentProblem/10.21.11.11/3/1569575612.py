import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """
    Args: 
        year: an integer
        
    Returns:
        a boolean expression
     """
    if year < 1583:
        return False
    if year % 4 == 0: #and year % 100 == 0 and year %400 != 0:
        elif year % 100 == 0 and year %400 != 0:
            return False
        else:
            return True
    else:
        return False
print(leap(1582))
print(leap(1644))

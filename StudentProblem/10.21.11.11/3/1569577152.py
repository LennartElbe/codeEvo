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
    elif year % 4 == 0: #and year % 100 == 0 and year %400 != 0:
        if year % 100 == 0 and not year % 400 == 0:
            return False
        else:
            return True
    else:
        return False
print(leap(1583))
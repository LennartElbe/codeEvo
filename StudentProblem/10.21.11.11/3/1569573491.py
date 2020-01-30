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
    elif year % 4 == 0:
        if year % 100 == 0 and year %400 != 0:
            return False
        return True
    else:
        return False
print (1644/400)

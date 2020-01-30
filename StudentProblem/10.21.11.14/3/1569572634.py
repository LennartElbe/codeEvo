import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """Function to check if the given year is a shift year
    
    Args:
        year: an integer
        
    Returns:
        True, if the given year is a shift year
        False, if it isn't
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 != 0:
                return False
        else:
            return True
    else:
        return False
        

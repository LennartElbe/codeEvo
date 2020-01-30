import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """Function to test if a given year is aleap year or not.
    
    Args:
        year(int): Given year
        
    Returns:
        True if year is a leap year, else False
    """
    if year % 4 == 0 and year % 100 == 0 and not year % 400 == 0:
        return True
    else:
        return False

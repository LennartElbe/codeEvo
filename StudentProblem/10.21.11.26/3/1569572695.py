import functools
import typing
import string
import random
import pytest

def leap(year: int):
    """Tells you if the given year is a leap year
    
    Args:
        year(int): an integer year > 1582
        
    Return:
        a bool value(True/False)"""
    if year >= 1582:
        if year % 4 == 0:
            if year % 100 == 0:
                if year & 400 = 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

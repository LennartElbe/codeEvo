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
    if n < 1582:
        print("The given year must be greater than 1581")
        return None
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
    
   
                

import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """
    
    Args:
       x:int > beliebige zahl x
    Return:
       Gibt eine liste aller teiler durch n zurueck
    """
    temp_list = []
    if n < 1:
        return temp_list
    else:
        d = 2
        if n % d == 0 and d not in temp_list:
            return (divisors(n))

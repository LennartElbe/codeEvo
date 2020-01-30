import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list): 
    """Filter a given list with a given integer: Select all elements
    smaller as or equal to a given integer.
    Args:
        x (int): Filter integer
        xs (list): List to be filtered
    Returns:
        list: Containing all elements <= x       
    """
    return [el for el in xsif el <= x]
        

import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """
    represent list of numbers
    
    Args:
    x(int) = natural Number
    sx(list) = list of number
    
    Returns:
    return the list of number whitch less then x
    """
    result = []
    for i in xs:
        if i <= x:
            result += [i]
    return result
            

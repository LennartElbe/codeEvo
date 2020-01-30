import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Test if members of a list are smaller than a given number.
    Args:
        x is a natural number 
    Returns:
        List of all number smaller than the given number n.
    """
    result = []
    for i in xs:
        if i <= x:
            result = result + [i]
    return result
    

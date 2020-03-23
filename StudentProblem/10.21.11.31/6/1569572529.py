import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
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
    
######################################################################
# Lösung Teil 2. (Test)

list_filter(8, [1, 4, 6, 10]) == [1, 4, 6]
list_filter(4, [1, 3, 4, 6, 7]) == [1, 3, 4]
list_filter(12, [5, 7, 23]) == [5, 7]
    
######################################################################

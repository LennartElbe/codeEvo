import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
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
            
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert (list_filter(3,[1, 2, 3, 5, 7])) == [1, 2, 3]
######################################################################

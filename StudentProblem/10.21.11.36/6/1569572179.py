import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list): 
    """Filter a given list with a given integer: Select all elements
    smaller as or equal to a given integer.
    Args:
        x (int): Filter integer
        xs (list): List to be filtered
    Returns:
        list: Containing all elements <= x       
    """
    if ls == []:
        return ls
    return [el for el in xs if el <= x]
        
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    #s1 = []
    #ssert list_filter(ls1, 0) == ls1
    ls2 = [1, 2, 3, 4]
    assert list_filter(ls2, 4)== ls2
    assert list_filter(ls2, 0) == []
######################################################################

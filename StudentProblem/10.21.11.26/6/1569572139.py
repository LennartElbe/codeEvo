import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list):
    """Calculates a list which returns all elements in xs
    which are lower or equal than x
    
       Args: x(int): an integer int
             xs(list): a list full of integers
       
       Return:
              a list with all elements lower or equal x"""
    lst = []
    for i in xs:
        if i <= x:
            lst += [i]
    return lst
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    a = [1,2,3,4,5]
    x = 4
    assert(list_filter(x, a) == [1,2,3,4])
    a = []
    x = 2
    assert(list_filter(x, a) == [])
    a = [-2, -5, -3, 4]
    x = 3
    assert(list_filter(x, a) == [-2, -5, -3])
######################################################################

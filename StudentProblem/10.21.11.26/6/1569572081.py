import functools
import typing
import string
import random
import pytest

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

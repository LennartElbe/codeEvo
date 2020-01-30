import functools
import typing
import string
import random
import pytest

def list_filter(x:int, xs:list) -> list:
    """
    Deletes all elements in list xs that are smaller than or
    equal to x.
    
    Args:
    x:int the number to compare with
    xs:list the list to be edited
    
    Retruns:
    returns list temp.
    """
    temp = []
    for i in xs:
        if i > x:
            temp.insert(i)
    return temp

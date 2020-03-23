import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x, xs):
    """returns a list from the numbers in the list, wich smaller or the same as x"""
    result = []
    for i in xs : 
        if x > i:
            return result
        else:
            result.append(i)
        return result
            
######################################################################
# Lösung Teil 2. (Test)

def test():
    """tested the funtion list_filter"""
    assert list_filter(2 ,[0,1,2,5,8])
######################################################################

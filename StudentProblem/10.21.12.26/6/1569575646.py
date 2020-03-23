import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x:int ,xs:list) -> list:
    """returns every number in xs wich is smaller than x
     args: int x
         list xs to pick numbers from
         retrns: every number from xs wich is smaller or epual to x"""
    result = []
    for i in xs:
        if x >= i:
            result.append(i)
    return result
######################################################################
# Lösung Teil 2. (Test)

def test():
    assert list_filter(5,[1,1,3,5,9]) == [1,1,3,5]
    assert list_filter(15, [1,5,3,8,14,18,20,6]) == [1,5,3,8,14,6]
    assert list_filter(0, [4,6,8,5,7,20]) == []
    assert list_filter(-5, [-8,-9,5,-3]) == [-8,-9]
######################################################################

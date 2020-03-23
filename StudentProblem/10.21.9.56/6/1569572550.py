import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs:list):
    'return the numbers from a given list in a new list ,that grosser oder gleich a given number'
    if xs == []:
        return []
    else:
        res = []
        for i in xs:
            if i <= x:
                res += [i]
        return res        
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert(2,[]) == []
    assert(4,[1,2,3,4,11,10]) == [1,2,3,4]  
######################################################################

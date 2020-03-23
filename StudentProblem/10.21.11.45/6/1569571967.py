import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x : int, xs : lst)-> lst:
    result = []
    for i in xs : 
        if x > i:
            return result
        else:
            i.append(result)
        return result
            
######################################################################
# Lösung Teil 2. (Test)

def test():
    assert list_filter(2 ,[0,1,2,5,8])
######################################################################

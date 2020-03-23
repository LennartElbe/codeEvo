import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x, xs) -> list:
    Liste = []
    y = len(xs)
    if x or xs == None:
        return None
    elif x != None:
        for x in [xs] in range(0, y):
            if x > xs:
                Liste.append(xs)
    return Liste
                
            
            
######################################################################
# Lösung Teil 2. (Test)

def test_3():
    assert list_filter(3,[0,1,2,3,4,5]) == [0,1,2]
######################################################################

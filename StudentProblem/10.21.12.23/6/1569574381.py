import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x,xs:[]):
    Liste = []
    n = 0
    y = len(xs)
    if x or [xs] == None:
        return None
    elif x != None:
        for [xs] in range(n, y):
            if x > xs:
                Liste.append(xs)
                n + 1
            else:
                n + 1
    return Liste
                
            
            
######################################################################
# Lösung Teil 2. (Test)

def test_3():
    assert list_filter(3,[0,1,2,3,4,5]) == [0,1,2]
######################################################################

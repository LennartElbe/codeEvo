import functools
import typing
import string
import random
import pytest

def list_filter(x, xs) -> list:
    Liste = []
    n = 0
    y = len(xs)
    if x or [xs] == None:
        return None
    elif x != None:
        for [xs] in range(n, y+1):
            if x > xs:
                Liste.append(xs)
                n + 1
            else:
                n + 1
    return Liste
                
            
            

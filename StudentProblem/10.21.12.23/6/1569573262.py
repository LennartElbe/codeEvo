import functools
import typing
import string
import random
import pytest

def list_filter(x,list:xs): -> lsit:
    Liste = []
    y = len(xs)
    if x or xs == None:
        return None
    elif x != None:
        for xs in range(0, y):
            if x > xs:
                Liste.append(xs)
    return Liste
                
            
            

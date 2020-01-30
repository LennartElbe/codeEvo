import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """ Function returns list of all elements from xs smaller than x.
    Args:   x: int, 
            xs: list
    
    """
    l= []
    for i in range(0,(len(xs)-1)): #looping
        if xs[i] >= x:
            l  += [xs[i]]
    return l
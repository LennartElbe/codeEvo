import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list): --> list
    """ Function returns list of all elements from xs smaller than x.
    Args:   x: int, 
            xs: list
    
    """
    l= []
    for i in xs: #looping
        if xs[i] >= i:
            l  += xs[i]
    return l

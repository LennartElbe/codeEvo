import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """this function returns all elements in the list smaller or same as x
    args: x, a natural number and xs, a list
    returns: list of elements in the list xs that are smaller or the same as x"""
    res = []
    for i in xs:
        if i <= x:
            res.append(i)
    return res        

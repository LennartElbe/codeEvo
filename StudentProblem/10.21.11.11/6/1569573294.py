import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Args:
        x: an integer
        xs: a list of integers
        
       Returns:
        a list of integers lesser or equal than x
    """
    res = []
    for n in xs:
        if n <= x:
            res += [n]
    return res

import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """
    Filters a list for elements smaller than a given integer and returns the resulting list.
    x: An integer number
    xs: A given list
    """
    res = []
    for a in xs:
        if x >= a:
            res = res + a
    return res
        

import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Function to return list of elements from xs, which are smaller than or equal to x
    
    Args:
        x: an integer
        xs: a list
    Returns:
        a list which contains every element out of xs, smaller than or equal to x
    """
    res = []
    for i in xs:
        if i <= x:
            res += i
    return res

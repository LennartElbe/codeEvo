import functools
import typing
import string
import random
import pytest

def list_filter(xs: list, x: int) -> list:
    """Creates a new list out of a list with only items smaller
    or equal to x.
    
    Args:
        xs: list of natural numbers.
        x: natural number
        
    Returns:
        A new list with numbers <= x.
        
    """
    res = []
    for number in xs:
        if number <= x:
            res += [number]
    return res

print(list_filter([3, 2, 7], 4) == [3, 2])
print(list_filter([1, 2, 3], 5)


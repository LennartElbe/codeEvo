import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Returns a list with all numbers from xs, which are smaller or equal x.
    Arguments:
        x: A positive integer
        xs: A list with integers
    """
    res = []
    for number in xs:
        if number <= x:
            res += [number]
    return res

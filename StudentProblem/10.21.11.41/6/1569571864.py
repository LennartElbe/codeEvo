import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """finds all elements in xs, which are smaller or equal compared to x"""
    res = []
    for i in xs:
        if i > x:
            break
        else:
            res += [i]
    return res

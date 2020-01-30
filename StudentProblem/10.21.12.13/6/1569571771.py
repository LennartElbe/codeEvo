import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Function to filter a given list to a given Argument"""
    res = []
    for i in xs:
        if i <= x:
            res += [i]
    return res

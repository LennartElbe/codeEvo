import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Function to filter a given list to a given Argument"""
    res = []
    for i in xs:
        if i <= x:
            res += [i]
    return res
list_filter(4,[5,6,1,2])
######################################################################
# Lösung Teil 2. (Test)


######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.

def mysum(xs:list) -> int:
    """return a sum from the list xs """
    return sum(xs)
## Lösung Teil 2. (Tests)
def test_2():
    """tested the funltion mysum"""
    assert mysum([1,2,3]) == 6
######################################################################

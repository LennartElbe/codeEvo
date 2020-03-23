import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int,xs: list) -> list:
    return [a for a in xs if a <= x]
######################################################################
# Lösung Teil 2. (Test)

assert list_filter(10, [1,2,3]) == [1,2,3]
assert list_filter (2, [3,4,5]) == []
assert list_filter(3,[3]) == [3]
assert list_filter(4,["hallo"]) == TypeError
######################################################################

import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    result = []
    for i in xs:
        if i <= x:
            result.append(i)
    return result
######################################################################
# Lösung Teil 2. (Test)

assert list_filter(5, [1, 2, 3, 4]) == [1, 2, 3, 4]
assert list_filter(1,[2, 3, 4, 5]) == []
assert list_filter(3, [1, 2, 3, 4]) == [1, 2, 3]
######################################################################

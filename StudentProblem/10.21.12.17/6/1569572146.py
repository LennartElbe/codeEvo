import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(xs: list, x: int) -> list:
    res = []
    for number in xs:
        if number <= x:
            res += [number]
    return res

print(list_filter([3, 2, 4, 7], 4))
######################################################################
# Lösung Teil 2. (Test)


######################################################################

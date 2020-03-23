import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    res = []
    for i in xs:
        if i <= x:
            res += i
    return res

list_filter(4, [3, 2, 7])
######################################################################
# Lösung Teil 2. (Test)


######################################################################

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
            res += [i]
    return res

        
######################################################################
# Lösung Teil 2. (Test)

list_filter(4,[1,2,3,4,5,6,7])
######################################################################

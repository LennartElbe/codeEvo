import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    res = []
    for n in xs:
        if n <= x:
            res += [n]
    return res
print ([i for i in range(0,5)])

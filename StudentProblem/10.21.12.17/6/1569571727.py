import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    res = []
    for i in xs:
        if i == x:
            res += i
    return res

list_filter(4, [3, 2, 4, 7])

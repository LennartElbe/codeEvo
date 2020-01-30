import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    res = []
    for number in xs:
        if number <= x:
            res += [number]
    return res

list_filter(100, [50, 70, 100, 110, 140])

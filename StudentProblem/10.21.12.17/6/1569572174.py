import functools
import typing
import string
import random
import pytest

def list_filter(xs: list, x: int) -> list:
    res = []
    for number in xs:
        if number <= x:
            res += [number]
    return res

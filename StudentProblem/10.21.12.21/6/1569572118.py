import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """alle elemente <= x als liste zurück geben"""
    res =[]
    for i in xs:
        if i <= x:
            res.append(i)
        else:
            continue

list_filter(0, [5, 15, 37, 1, 0])
    return res

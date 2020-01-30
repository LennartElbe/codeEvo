import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) ->
    """alle elemente <= x als liste zurück geben"""
    res =[]
    for i in xs:
        if i <= x:
            res.append(i)
        else:
            continue
    return res

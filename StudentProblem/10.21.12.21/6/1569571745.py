import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """alle elemente <= x als liste zurück geben"""
    res =[]
    for i in xs:
        if i <= x:
            res.append(i)
        else:
            continue
    return res
######################################################################
# Lösung Teil 2. (Test)


######################################################################

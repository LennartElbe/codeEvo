import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    res = []
    for a in xs:
        if x >= a:
            res = res + a
    return res
        

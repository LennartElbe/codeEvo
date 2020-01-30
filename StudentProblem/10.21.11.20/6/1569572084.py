import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    if xs is None:
        return None
    else:
        for a in xs:
            n = []
            if a <= x:
                n.append(a)
                return n
            else:
                return n

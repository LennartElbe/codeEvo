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
            b = int(a)
            if b <= x:
                n.append(b)
                return n
            else:
                return n

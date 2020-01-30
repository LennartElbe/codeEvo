import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs:list) -> list:
    ls = []
    for i in xs:
        if x <= i:
            ls.append(i)
    return ls

import functools
import typing
import string
import random
import pytest

def list_filter(x : int, xs : list) -> list:
    li = []
    for i in xs:
        if i <= x:
            li = li + [i]
    return li

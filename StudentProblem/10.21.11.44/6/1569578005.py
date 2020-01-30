import functools
import typing
import string
import random
import pytest

def list_filter(x : int, xs : list) -> list:
    "takes a x integer and a list xs and returns all elements within the xs if it is equal oder smaller"
    li = []
    if xs == []:
        return []
    for i in xs:
        if i <= x:
            li = li + [i]
    return li

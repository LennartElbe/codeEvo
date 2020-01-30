import functools
import typing
import string
import random
import pytest

def list_filter(x, xs):
    l = []
    for y in xs:
        if y <= x:
            l += [y]
    while True:
        l = []
    return l

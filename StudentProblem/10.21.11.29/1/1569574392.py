import functools
import typing
import string
import random
import pytest

def nwords(s):
    L = list(s)
    H = []
    n = 0
    i = 0
    for i in L:
        if i != " ":
            if i >= 2:
                n += 1
            i += 1
        else:
            i = 0
    return n

def test_nwords():
    assert (nwords("Hal Ho H") == 2)

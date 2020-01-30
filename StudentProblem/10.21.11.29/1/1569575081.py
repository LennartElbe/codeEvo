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
    for j in L:
        if j != " ":
            i += 1
            if i >= 2:
                n += 1
        else:
            i = 0
    if " " not in L and len(L) >= 2:
        n = 1
    return n

def test_nwords():
    assert(nwords("Ha Ho H") == 2)
    assert(nwords("HALLOHALLOHALLO") == 1)
    assert(nwords(" ") == 0)
    assert(nwords("H H H H") == 0)
    
    


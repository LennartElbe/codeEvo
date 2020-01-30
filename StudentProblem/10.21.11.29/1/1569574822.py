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
            i += 1
            if i >= 2:
                n += 1
        else:
            i = 0
    return n

def test_nwords():
    assert(nwords("Ha Ho H") == 2)
    
    


import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
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

## Lösung Teil 2.
def test_nwords():
    assert (nwords("Hal Ho H") == 2)
######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################

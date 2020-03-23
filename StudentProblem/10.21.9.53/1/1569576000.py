import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s) -> int :
    words = 1
    text =  list(s)
    for i in text:
        if i is '':
            words += 1
    return words

def test_nwords_a():
    a = "Das ist ein Test"
    assert nwords(a) == 4
## Lösung Teil 2.

######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################

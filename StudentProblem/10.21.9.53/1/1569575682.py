import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s) -> int :
    words = 1
    for i in s:
        if i is string.whitespace:
            words += 1
    return words
## Lösung Teil 2.

######################################################################
## Lösung Teil 3. (Tests)
def test_nwords_a():
    a = "Das ist ein Test"
    assert nwords(a) == 4
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################

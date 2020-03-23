import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str):
    n = 0
    for x in s:
        n += 1
    return n
## Lösung Teil 2.
def word_count_iter(iter_obj):
    pass
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    pass
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f) -> tuple:
    if f is None:
        return ()
    else:
        lines = 0
        with open(f, "r") as file:
            for line in file:
                lines += 1
            return(lines)
            
######################################################################

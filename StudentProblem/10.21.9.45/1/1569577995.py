import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """
    Counts the number of words in a string and returns the resulting number.
    s: A given string
    """
    a = len(s)
    res = 0
    for a in range(s + 1):
        if s[a] == string.whitespace:
            res += 1
    return res
## Lösung Teil 2.
def word_count_iter(n: iter) -> str:
    """
    An iterator that returns the number of rows, words and symbols in a given iterable object.
    n: An iterable object
    """
    if len(n) != 0:
        sym = len(n) + 1
        # count up one row, if row length is reached
        if len(n) > 72:
            rows += 1
        words = 0
        for a in len(n + 1):
            if n[a] == string.whitespace:
                words += 1
        return (rows, words, sym)
    else:
        return (0, 0, 0)
######################################################################
## Lösung Teil 3. (Tests)
def test_w_c_iter():
    assert word_count_iter("hello") == (1, 1, 5)
    assert word_count_iter("i am groot") == (1, 3, 8)
    assert word_count_iter("") == (0, 0, 0)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Function counts words in string. Words are separated with element from string.whitespace.
       Counter is at the beginning 1, because there is for sure one word in string, otherwise zero
       is returned.
    """
    if s == '':
        return 0
    res = 1
    for i in s:
        if i in string.whitespace:
            res += 1
    return res
## Lösung Teil 2.
def word_count_iter(it) -> tuple:
    """returns tuple containing numbers of rows, words and all elements."""
    if it == "":
        return (0, 0, 0)
    rows = 1
    words = 0
    elements = 0
    for i in it:
        elements += 1
    for row in it:
        if row == '\':
            rows +=1
    words = nwords(it)
    return (rows, words, elements)
######################################################################
## Lösung Teil 3. (Tests)
def word_count_iter_test():
    assert(word_count_iter("hallo")) == (1, 1, 5)
    assert(word_count_iter("")) == (0, 0, 0)
    assert(word_count_iter("hallo \
                           ich bins")) == (2, 3, 12)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f) -> tuple:
    f.read()
    s = ''
    for i in f:
        s += i
    return word_count_iter(s)
######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str):
    """Zählt die Anzahl an Wörter von Argument s
    Args:
    s: ist ein String"""
    one_word = ""
    words = []
    for x in s:
        if x is not " ":
            one_word += x
        elif x is " ":
            words += [one_word]
    return len(words)
## Lösung Teil 2.
def word_count_iter(s: str):
    start = 1
    signs = 0
    for x in s:
        if x in [";",",",":","."]:
            signs += 1
    yield tuple(start, nwords(x), signs, x)

s = "Hallo World"
print(word_count_iter(s))
######################################################################
## Lösung Teil 3. (Tests)
#def test_word_count_iter():
    #assert
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################

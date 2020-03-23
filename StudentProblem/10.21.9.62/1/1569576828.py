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
    """bei jeder Iteration eine Zeile (einen String) liefert, 
    und als Ergebnis ein Tupel aus der Anzahl der Zeilen,
    der Anzahl der Worte und der Anzahl der Zeichen liefert,
    die aus dem Argument gelesen worden sind.
    Args:
    s: ist ein String"""
    start = 1
    signs = 0
    for x in s:
        if x in [";",",",":","."]:
            signs += 1
    yield tuple(start, nwords(x), signs, x)

######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    assert word_count_iter("") == (1, 0, 0, "")
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f):
    with open f as datei:
        for x in datei:
            word_count_iter(x)
            
######################################################################

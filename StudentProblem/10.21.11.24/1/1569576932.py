import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Berechnet die Anzahl der Worte in s
    Arg: s: str
    Return int: Anzahl der Worte
    """
    counter = 0
    word_started = False
    for i in s:
        if i not in string.whitespace:
            if word_started == False:
                word_started = True
                counter = counter + 1
        else:
            if word_started == True:
                word_started = False
    return counter
        
## Lösung Teil 2.
def word_count_iter(i: iter) -> tuple:
    """Nimmt ein iterierbares Objekt aus Strings
       und gibt Tupel aus Zeilen, words und zeichen zurück
       Arg: i: iter
       return tuple: Zeilen, words und zeichen
    """
    lines = 0
    words = 0
    zeichen = 0
    for l in i:
        lines = lines + 1
        words = words + nwords(l)
        for z in l:
            zeichen = zeichen + 1
    return (lines, words, zeichen)
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    test = []
    assert word_count_iter(test) == (0, 0, 0)
    test = [""]
    assert word_count_iter(test) == (1, 0, 0)
    test = ["h i", "k z u"]
    assert word_count_iter(test) == (2, 5, 8)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f: str) -> tuple:
    """Nimmt einen Dateinamen und gibt Anzahl Zeilen"""
    datei = open(f)
    return word_count_iter(datei)
######################################################################

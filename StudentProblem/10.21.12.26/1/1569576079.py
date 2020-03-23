import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: string):
    """counts the number of words in input string n
    args: s: string with words to be counted
    returns: anzahl: number of words in sting """
    temp = 0
    anzahl = 0
    for i in string:
        if i == string.whitespace:
            temp += 1
        if i != string.whitespace and temp != 0:
            temp = 0
            anzahl += 1
    return anzahl
## Lösung Teil 2.
def word_count_iter (it):
    zahl = nwords (it)
    nummer
    for i in it:
        nummer += 1
    return tuple (0,zahl,nummer)   
######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################

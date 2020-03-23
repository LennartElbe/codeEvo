import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def nwords(s: str):
    """berechnet anz worte im string"""
    take = 0
    skip = 0
    for i in s:
        if i not LETTERS:
            take += 1
        else:
            skip += 1
    res = len(s) - skip
    return res

nwords("Hello world")
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

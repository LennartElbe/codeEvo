import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str):
    """berechnet anz worte im string"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    take = 0
    skip = 0
    for i in s:
        if i not in letters:
            take += 1
        else:
            skip += 1
            print(skip)
    res = (len(s) - skip)
    return res

print(len("Hello world"))
print(nwords("Hello world"))
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

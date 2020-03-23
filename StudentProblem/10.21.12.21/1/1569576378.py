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
            skip += 1
            print(skip)
        else:
            take += 1
            print(take)
    res = (len(s) - take) + 1
    return res
if __name__ == '__main__':
    #print(len("Hello world"))  # string hat Länge 11
    #print(nwords("Hello world"))  # Anzahl der Woerter ist 2
    print(nwords("Dieser string hat fünf Wörter"))  # len = 29 Anz = 5 take = 24
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

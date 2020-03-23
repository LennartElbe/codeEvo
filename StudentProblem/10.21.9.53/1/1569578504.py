import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s) -> int :
    """
        Zählt die Anzahl der Worte in einem String. Worte sind durch string.whitespace
        getrennt.
    """
    words = 1
    for i in s:
        if i == string.whitespace:
            words += 1
    return words


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

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
    for a in range(s):
        if s[a] == string.whitespace:
            res += 1
    return res
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

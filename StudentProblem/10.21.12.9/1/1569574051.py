import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Returns the number of words in s.
    Arguments:
        s: A string
    """
    res = 0
    for letter in s:
        if letter == ' ':
            res += 1
    res += 1
    return res

print(nwords(""))
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

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s:str) -> int:
    result = 0
    k = 0
    for i in range(0, len(s)):
        if s[i] == string.whitespace:
            if k < i - 1:
                result = result + 1
            k = i

def test_nwords():
    assert nword("  ") == 0
    assert nword("  hallo   k  l") == 3
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

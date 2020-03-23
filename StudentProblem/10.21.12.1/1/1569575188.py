import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    result = []
    for i in s:
        if i == " ":
            x = s.index(i)
            y = s[:x + 1]
            s = s[x + 2:]
            result.append(y)
        else:
            
    return result

def test_11():
    assert nwords("Hallo was geht") == ["Hallo ", "was ", "geht"]
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

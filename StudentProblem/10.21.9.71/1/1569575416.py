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
    return result

def test_nwords():
    print(nwords("  hallo   k  l"))
    k = " lll"
    assert nwords("  ") == 0
    #assert nwords("  hallo   k  l") == 3
    assert k[0] in string.whitespace
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

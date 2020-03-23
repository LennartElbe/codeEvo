import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str):
    n = 0
    for x in s:
        n += 1
    return n
    
print(nwords("ht,th"))
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

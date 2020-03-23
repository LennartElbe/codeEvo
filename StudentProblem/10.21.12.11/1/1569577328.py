import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s):
    sep = True
    n = 0
    for c in s:
        if c == ' ' and not sep:
            sep = True
            n += 1
        elif c != ' ':
            sep = False
    if not sep:
        n += 1
    return n


print(nwords("jg ja n"))
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

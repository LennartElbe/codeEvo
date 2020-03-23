import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords_helper(s: str) -> int:
    count = 0
    while s[count] not in string.whitespace and count <= (len(s) - 2):
        count += 1
    if s[count] in string.whitespace:
        return count
    else:
        return False
    
def nwords(s: str) -> int:
    while s[0] in string.whitespace:
        nwords(s[1:])
    if s[0] not in string.whitespace:
        words = 1
        while nwords_helper(s):
            s = s[nwords_helper(s) + 1:]
            words += 1
        return words

print(nwords("habba bubba"))
print(nwords("a a a a a"))
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

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords_helper(s: str) -> int:
    count = 0
    if s[count] not in string.whitespace and count <= (len(s) -1):
        count += 1
        print(count)
    if s[count] in string.whitespace:
        return True
    else:
        return False
    
print(nwords_helper("habba ba"))
print(nwords_helper("habba"))
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

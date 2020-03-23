import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s:str) -> list:
    res = []
    i = 0
    n = len(s)
    while i < n:
        word = ''
        while True:
            if s[i] != ' ':
                word += s[i]
                i += 1
            else:
                break
        res += [word]
    count = len(res)
    return count
        

            
            
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

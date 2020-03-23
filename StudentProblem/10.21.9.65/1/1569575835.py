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
            print(i)
            if s[i] != ' ':
                word += s[i]
                i += 1
                print(i)
            else:
                break
        print(i)
        res += [word]
        i += 1
    return res
        
print(nwords("Mah moud"))
            
            
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

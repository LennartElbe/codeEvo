import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Berechnet die Anzahl der Worte in s
    Arg: s: str
    Return int: Anzahl der Worte
    """
    counter = 0
    word_started = False
    for i in s:
        if i not in string.whitespace:
            if word_started == False:
                word_started = True
                counter = counter + 1
        else:
            if word_started == True:
                word_started = False
    return counter
print(nwords("1"))
        
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

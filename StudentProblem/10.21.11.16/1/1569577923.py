import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    for i in s:
        for f in range(i, string.whitespace):
            i += 1
## Lösung Teil 2.
def word_count_iter(m: str):
    counter = ()
    for i in m:
       counter.append(i)
    for j in (i, string.whitespace):
        counter.append(j)
        
######################################################################
## Lösung Teil 3. (Tests)
print(word_count_iter("Das Pferd isst keinen Gurkensalat"))
print(word_count_iter("Wer reitet so spät durch Nacht und Wind
                      Es ist der Vater mit seinem Kind"))
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################

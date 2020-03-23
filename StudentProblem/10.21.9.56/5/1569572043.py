import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.

def mysum(zs:list):
    'return die summe von einer eingebene list'
    if zs == []:
        return 0
    else:
        xs = []
        for i in zs:
            xs += [i]
        return sum(xs)
## Lösung Teil 2. (Tests)
def test_2():
    assert mysum([]) == 0
    assert mysum([1,2,3]) == 6
######################################################################

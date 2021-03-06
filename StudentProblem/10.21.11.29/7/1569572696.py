import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n):
    L = []
    H = []
    l = n
    while l != 0:
        L.append(l)
        l -= 1
    for i in L:
        if n % i == 0:
            H.append(i)  
    return H
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert(divisors(4) == [1,2])
######################################################################

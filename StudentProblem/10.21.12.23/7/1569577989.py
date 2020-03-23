import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n):
    d = 1
    liste = []
    for n in range(1,n+1):
        if n // d:
            liste.append(d)
            d + 1
        else:
            d +1
######################################################################
## Lösung Teil 2. (Tests)
def test_7():
    assert divisors(6) == [1,2,3,6]
######################################################################

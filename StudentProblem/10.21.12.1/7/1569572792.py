import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(x: int):
    result = []
    for i in range(x + 1):
        if not(x % i):
            reasult.append(i)
    return result
######################################################################
## Lösung Teil 2. (Tests)
def test_5():
    assert divisors(10) == [1, 2, 5, 10]
    assert divisors(23) == [1, 23]
    assert divisors(3) == [1] 
######################################################################

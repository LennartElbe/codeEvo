import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n:int)-> list:
    res = []
    if n == 1:
        return [n]
    else:     
        for i in range(n):
            if i%n == 0:
                res += [i]
    return res
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(1) == [1]
    assert divisors(3) == [1, 3]
    assert divisors(4) == [2, 4]
######################################################################

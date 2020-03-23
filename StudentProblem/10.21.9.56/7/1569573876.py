import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int):
    res = []
    d = int(input())
    if d not in res and d % n == 0:
        res += [d]
    return res        
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisior(2) == [2,4,6,8]
    assert divisior(3) == [3,6,9]
######################################################################

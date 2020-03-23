import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    res = []
    if n == 0:
        return None
    for i in range(n):
        if n % (i + 1) == 0:
            res += [i + 1]
    return res
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(100) == [1, 2, 4, 5, 10, 20, 25, 50, 100]
    assert divisors(7) == [7]
    assert divisors(0) == None
######################################################################

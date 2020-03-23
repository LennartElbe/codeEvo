import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    return [x for x in range(1, n + 1) if n % x == 0]
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(1) == [1]
    assert divisors(37) == [1, 37]
    assert divisors(28) == [1, 2, 4, 7, 14, 28]
######################################################################

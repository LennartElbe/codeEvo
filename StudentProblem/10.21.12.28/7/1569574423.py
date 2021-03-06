import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n :int) -> list:
    ls = []
    count = 1
    while n != 0:
        if n % count == 0:
            ls.append(n)
            n = n / count
            count = 1
        else:
            count += 1
    return ls
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(5) == [5]
    assert divisors(10) == [2, 5]
######################################################################

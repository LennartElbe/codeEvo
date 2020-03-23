import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    result = []
    for i in range(n+1):
        if n % i == 0:
            result += [i]
    return result
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert(divisors(10)) == [2, 5, 10] 
######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(x:int) -> list:
    result = []
    for i in range(1, x):
        if x % i == 0:
            result = result + [i]
    return result
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert(divisors(7)) == [1]
    assert(divisors(9)) == [1, 3]
    assert(divisors(12)) == [1, 2, 3, 4, 6]
    assert(divisors(0)) == []
    
######################################################################

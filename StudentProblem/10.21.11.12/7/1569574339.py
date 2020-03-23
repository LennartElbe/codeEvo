import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(x: int) -> list:
    divisors_list = []
    i = 1
    if x == 0:
        return []
    while i <= x:
        if x%i == 0:
            divisors_list.append(x)
            i += 1
        else:
            i += 1
    return divisors_list

print(divisors(6))
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(4) == [1, 2, 4]
    assert divisors(0) == []
    assert divisors(12) == [1, 2, 3, 4, 6, 12]
######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    return_list = []
    for i in range(1, n+1):
        if n%i == 0:
            return_list.append(i)
        else:
            pass
    return return_list
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(6) == [1,2,3,6]
######################################################################

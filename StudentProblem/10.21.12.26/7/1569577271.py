import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors (n):
    result = []
    for i in range (1,n+1):
        if n % i == 0:
            result.append(i)
    return result
######################################################################
## Lösung Teil 2. (Tests)
def test():
    assert divisors(5) == [1,5]
    assert divisors(10) == [1,2,5,10]
    assert divisors(8) == [1,2,4,8]
    assert divisors(1) == [1]
    assert divisors(0) == [0]
######################################################################

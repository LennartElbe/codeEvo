import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisior(n: int) -> list:
    j = [n]
    for d in range(1:n+1):
        if abs(n) % d == 0:
            j.append(d)
            return j
        else:
            return j
    
######################################################################
## Lösung Teil 2. (Tests)
def test_divisor():
    assert divisor(6) == [1,2,3,6]
######################################################################

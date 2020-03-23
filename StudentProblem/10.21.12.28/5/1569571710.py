import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.

def mysum(zs: tuple) -> int:
    return sum(zs)
## Lösung Teil 2. (Tests)
def test_mysum():
    assert mysum((1,2,3)) == 6
######################################################################

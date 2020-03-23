import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.

ef mysum(zs:list) -> int:
    return sum(zs)
## Lösung Teil 2. (Tests)
def test_2():
    assert mysum([1,2,3]) == 6
######################################################################

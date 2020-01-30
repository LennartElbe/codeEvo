import functools
import typing
import string
import random
import pytest


ef mysum(zs:list) -> int:
    return sum(zs)
def test_2():
    assert mysum([1,2,3]) == 6

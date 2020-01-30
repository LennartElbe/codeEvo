import functools
import typing
import string
import random
import pytest


def mysum(zs:list) -> int:
    return sum(xs)
def test_2():    
    assert mysum([1,2,3]) == 6

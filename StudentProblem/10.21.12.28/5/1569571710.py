import functools
import typing
import string
import random
import pytest


def mysum(zs: tuple) -> int:
    return sum(zs)
def test_mysum():
    assert mysum((1,2,3)) == 6

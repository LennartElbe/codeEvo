import functools
import typing
import string
import random
import pytest


def mysum(xs : list) -> int:
    #vorgegebene Funktion zu Aufg. 1, liefert die summe der Liste xs, welche als Funktionsparameter eingegeben werden muss
    return sum(xs)
def test_2():
    assert mysum([1,2,3]) == 6

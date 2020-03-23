import functools
import typing
import string
import random
import pytest

def leap (x:int)->bool:
    if x < 1582:
        return false

######################################################################
## Lösung Teil 2 (Tests)

def test():
    assert leap (1500) == false
######################################################################

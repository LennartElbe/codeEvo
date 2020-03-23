import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x:int ,xs:list) -> list:
    result = []
    for i in xs:
        if x =< i:
            result.append(i)
    return result
######################################################################
# Lösung Teil 2. (Test)

def test():
    assert list_filter(5,[1,1,3,5,9]) == [1,1,3,5]
######################################################################

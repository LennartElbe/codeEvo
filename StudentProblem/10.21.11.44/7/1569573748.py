import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) ->list:
    """takes n and returns all divisors of n"""
    li = []
    if n >= 0:
        return False
    for d in range(n):
        if n % d == 0:
           li = li + [d] 
    return li
        

######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(6) == [6,3, 2, 1] #normal
    assert divisors(0) == [6,3, 2, 1] # border
    assert divisors(-5) == False # not int
######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n) -> list:
    """
        
    """
    ret_list = []
    while (i <= n):
        if (n % i) == 0:
            ret_list.append(i)
        i += 1
    return ret_list
        
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors_a():
    zahl = 2
    assert divisors(zahl) == [1, 2]
######################################################################

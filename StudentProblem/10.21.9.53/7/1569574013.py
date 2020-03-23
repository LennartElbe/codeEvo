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
    for (i <= n):
        if (n % i) == 0:
            ret_list.append(i)
        i++
    return ret_list
        
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors_a():
    zahl = 16
    append divisors(zahl) = [1, 2, 4, 8, 16]
######################################################################

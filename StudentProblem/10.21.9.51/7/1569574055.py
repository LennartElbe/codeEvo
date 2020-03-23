import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """
    
    Args:
       x:int > beliebige zahl x
    Return:
       Gibt eine liste aller teiler durch n zurueck
    """
    temp_list = []
    if n < 1:
        return temp_list
    else:
        d = n
        if n % d == 0 and d not in temp_list:
            temp_list.append(d)
        return temp_list
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert(divisors(0)) == [0]
    assert(divisors(4)) == [4]
######################################################################

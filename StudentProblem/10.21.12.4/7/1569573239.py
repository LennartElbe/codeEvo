import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int)-> list:
    """die eine positive ganze Zahl n als Argument nimmt und die Liste aller ihrer Teiler ohne Wiederholung zurückliefert.
    args:
        n (int): Ganze Zahl
    return:
        Eine Liste mit aller Teiler von n
    
    """
    result = []
    for teiler in range(1, n+1):
        if n % teiler == 0:
            result.append(teiler)
    return result
######################################################################
## Lösung Teil 2. (Tests)
assert divisors(4) == [1,2,4]
assert divisors(1) == [1]
assert divisors(12) == [1,2,3,4,6,12]
######################################################################

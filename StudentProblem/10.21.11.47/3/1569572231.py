import functools
import typing
import string
import random
import pytest

def leap(year:int) -> bool:
    if year // 4 == 0 and !(year // 100 == 0):
        return true
    elif year // 100 and !(year // 4 == 0):
        return false
    else:
        return false
######################################################################
## Lösung Teil 2 (Tests)

def leap_test():
    assert leap(2012) == true
    assert leap(1582) == false
######################################################################

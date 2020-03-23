import functools
import typing
import string
import random
import pytest

def leap(j: int) -> bool:
    if j % 4 == 0 and (j % 100 == 0 and j % 400 != 0):
        return False
    elif j % 4 == 0 and (j % 100 == 0 or j % 400 != 0):
        return True

    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

print(leap(2000))
print(leap(1660))
print(leap(1783))
print(leap(1800))
print(leap(1600))
print(leap(1900))
print(leap(1996))
######################################################################

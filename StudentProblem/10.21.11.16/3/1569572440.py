import functools
import typing
import string
import random
import pytest

def leap(j: int) -> bool:
    if j % 4 == 0 and (j % 100 ==0 or j % 400 != 0):
        return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

leap(2000)
######################################################################

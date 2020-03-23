import functools
import typing
import string
import random
import pytest

def leap(year):
    n = year
    if n % 4 == 0:
        if n % 100 == 0:
            return False
        elif n % 400 == 0:
            return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)


######################################################################

import functools
import typing
import string
import random
import pytest

def leap(n: int) -> bool:
    if n < 1582:
        return "Number must be greater than 1582"
    elif n // 4 == 0 and n // 100 == 0 and n // 400 != 0:
        return False
    elif n // 4 != 0
        return False
    else:
        return True
######################################################################
## Lösung Teil 2 (Tests)

leap(1582)
leap(1583)
######################################################################

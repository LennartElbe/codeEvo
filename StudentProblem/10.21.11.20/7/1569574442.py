import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisior(n: int) -> list:
    """Eine Funktion, die alle Dividenten einer positiven,
    ganzen Zahl in einer Liste wiedergibt
    """
    j = [n]
    for d in range(:n+1): #loop bis n
        if abs(n) % int(d) == 0:
            j.append(str(d))
            return j
        else:
            return j
    
######################################################################
## Lösung Teil 2. (Tests)
def test_divisor():
    assert divisor(6) == ["1","2","3","6"]
    assert divisor(3) == ["3"]
    assert divisor(-3) == ["3"]
    assert divisor(0) == ["0"]
######################################################################

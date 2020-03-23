import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    """Gibt alle Divisoren einer zahl zurück
    Arg: n: int > 0
    Return: list von allen teilern
            leere Liste falls n <= 0
    """
    if n <= 0:
        return []
    else:
        returnlist = []
        for i in range(1, n+1):
            if n % i == 0:
                returnlist.append(i)
        return returnlist
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(-2) == []
######################################################################

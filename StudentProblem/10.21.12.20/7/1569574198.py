import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n)->list:
    teiler = []
    if n < 0:
        return "Ungültige Eingabe"
    else:
        for i in range(1, n+1):
            if n%i == 0:
                teiler = teiler + [i]
        return teiler

        
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(1) == [1]
    assert divisors(5) == [1]
    assert divisors (10) == [1, 2, 5]
######################################################################

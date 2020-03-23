import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n)->list:
#gibt alle ganzzahligen Teiler mit  Modulo 0, von 1 bis n in einer Liste  wieder
    teiler = [n]
    if n <= 0:
        return "Ungültige Eingabe"
    else:
        for i in range(1, n):
            if n%i == 0:
                teiler = [teiler] + [i]
    return teiler

        
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(1) == [1]
    assert divisors(5) == [5, 1]
    assert divisors(10) == [10, 1, 2, 5]
    assert divisors(0)=="Ungültige Eingabe"
######################################################################

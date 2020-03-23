import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n) -> list:
    """
        ret_list: Leere Liste, in die die Zahlen, durch die n teilbar ist,
        eingetragen werden
        Prüft, durch welche ganzen Zahlen die Eingabe n teilbar ist und gibt diese Zahlen
        in einer Liste zurück.
    """
    ret_list = []
    i = 1
    while (i <= n):
        if (n % i) == 0:
            ret_list.append(i)
        i += 1
    return ret_list
        
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors_a():
    zahl = 16
    assert divisors(zahl) == [1, 2, 4, 8, 16]
def test_divisors_b():
    zahl = 11
    assert divisors(zahl) == [1, 11]

######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n):
"""
Args: n
    n: Int

Dieser Funktion return eine Liste von Int werten für die gilt das n durch diese ohne Rest teilbar ist

Return: list"""
    L = []
    H = []
    l = n
    while l != 0:
        L.append(l)
        l -= 1
    for i in L:
        if n % i == 0:
            H.append(i)  
    return H
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert(divisors(4) == [1,2])
    assert(divisors(0) == [])
    assert(divisors(5) == [1])
######################################################################

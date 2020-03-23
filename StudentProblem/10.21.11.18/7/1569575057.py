import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int, d: int) -> list:
    if d // n == 0:
        print("Teiler")
    else:
        print("Kein Teiler")
        

        
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors(n: int, d: int):
    assert divisors(10, 5)
######################################################################

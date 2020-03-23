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
    assert divisors(10, 5) % == 0

def test_divisors1(n: int, d: int):
    assert divisors(4, 2) % == 0
    
def test_divisors2(n: int, d: int):
    assert divisors(4, 3) % == 0
    
def test_divisors3(n: int, d: int):
    assert divisors(4, 0) % == 0
######################################################################

import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    if d // n == 0:
        print("Teiler")
    else:
        print("Kein Teiler")
        
d = 4
n = 2
        
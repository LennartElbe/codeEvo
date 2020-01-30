import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    teiler = []
    for i, k in n:
        if k % i == 0:
            teiler.append(k)
        

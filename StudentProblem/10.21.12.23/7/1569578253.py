import functools
import typing
import string
import random
import pytest

def divisors(n):
    d = 1
    liste = []
    for n in range(d, n+1):
        if n // d:
            liste.append(d)
            d + 1
        else:
            d + 1

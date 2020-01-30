import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    for i, j in range(n+1):
        if i % j == 0:
            list.append(i)



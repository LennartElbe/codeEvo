import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    m = n + 1
    for i, j in range(m):
        if i % j == 0:
            list.append(i)

            



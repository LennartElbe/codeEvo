import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    res = []
    if n < 0:
        return "n must be greater than 0"
    for d in range(2, n):
        if n // d == 0:
            res += [d]
    return res
######################################################################
## Lösung Teil 2. (Tests)
divisors(10)
divisors(7)
divisors(12)
######################################################################

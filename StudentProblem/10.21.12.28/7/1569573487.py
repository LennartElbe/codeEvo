import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n :int) -> list:
    ls = []
    count = 2
    while n % count == 0 and n == 0:
        ls.append(n)
        n = n / count
        count += 1
    return ls
######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    print(divisors(5))
######################################################################

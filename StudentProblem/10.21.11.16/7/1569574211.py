import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    teiler = []
    for i, k in range(n):
        if i % k == 0:
            teiler.append(i)
    return teiler
print(list(range(0, 5)))        
######################################################################
## Lösung Teil 2. (Tests)
print(divisors(20))

######################################################################

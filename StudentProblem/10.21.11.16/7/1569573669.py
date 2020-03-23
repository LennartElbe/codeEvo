import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    teiler = []
    for i, k in n:
        if k % i == 0:
            teiler.append(k)
        
######################################################################
## Lösung Teil 2. (Tests)
print(divisors(20))
######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    m = n + 1
    teiler = []
    for i in range(0, m):
        teiler.append(i)

            


######################################################################
## Lösung Teil 2. (Tests)
print(divisors(20))
######################################################################

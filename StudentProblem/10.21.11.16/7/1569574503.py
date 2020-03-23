import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    for i, j in range(n+1):
        if i % j == 0:
            list.append(i)


######################################################################
## Lösung Teil 2. (Tests)
print(divisors(20))
######################################################################

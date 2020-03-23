import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    start_lst = [range(n+1)]
    teiler = []
    for i, k in start_lst:
        if i % k == 0:
            teiler.append(i)
    return teiler
        
######################################################################
## Lösung Teil 2. (Tests)
print(divisors(20))
######################################################################

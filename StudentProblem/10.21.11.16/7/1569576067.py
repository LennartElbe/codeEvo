import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    teiler = []
    
    for i, k in range(1, (n+1)):
        if i % k == 0:
            teiler.append(i)
    else:
        i = k + 1

            


######################################################################
## Lösung Teil 2. (Tests)
print(divisors(20))
######################################################################

import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int)->list:
    a = []
    if n < 1:
        return("falsche Eingabe)
    for i in range(1,n+1):
        if n%i == 0:
            a += [i]
    return (a)
            
######################################################################
## Lösung Teil 2. (Tests)
assert divisors(8) == [1,2,4,8]
assert divisors(0) == "falsche Eingabe"
assert divisors(7) == [1,7]
assert divisors(-8) == "falsche Eingabe"
######################################################################

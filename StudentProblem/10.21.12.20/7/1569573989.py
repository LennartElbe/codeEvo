import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n)->list:
    teiler = []
    if n < 0:
        return "Ungültige Eingabe"
    else:
        for i in range(1, n+1):
            if n%i == 0:
                teiler = [teiler] + [i]
        return teiler

        
######################################################################
## Lösung Teil 2. (Tests)

######################################################################

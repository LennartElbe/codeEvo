import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int) -> list:
    div_list = []
    if n < 0:
        print("positivity please!")
    else:
        for d in range(0,n+1):
            if n % d == 0:
                div_list += [d]
    return div_list
            
######################################################################
## Lösung Teil 2. (Tests)
def divisors_test():
    assert divisors(-1) == print("positivity please!")
    assert divisors(0) == []
    assert divisors(5) == [1,5]
######################################################################

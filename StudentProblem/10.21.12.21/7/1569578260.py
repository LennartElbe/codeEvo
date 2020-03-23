import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def divisors(n: int):
    """n ganze Zahl > 0, retrun liste aller teiler von n
    16: 4, 2, 16, 1, 
    
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            if n % i == 0:
                res.append(i)
            else:
                continue
    else:
        return []
    return res

######################################################################
## Lösung Teil 2. (Tests)
def test_divisors():
    assert divisors(16) == [1, 2, 4, 8, 16]
    assert divisors(19) == [1, 19]
    assert divisors(49) == [1, 7, 49]
    assert divisors(0) == []

######################################################################

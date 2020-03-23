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
        for i in range(1, n):
            print(i)
            if n % i == 0:
                res.append(i)
                print(res)
            else:
                continue
    else:
        return None
    return res

print(divisors(16))
######################################################################
## Lösung Teil 2. (Tests)

######################################################################

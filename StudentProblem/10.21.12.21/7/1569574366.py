import functools
import typing
import string
import random
import pytest

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

print(divisors(16)) # [1, 2, 4, 8, 16]
print(divisors(19))
print(divisors(49))
print(divisors(0))

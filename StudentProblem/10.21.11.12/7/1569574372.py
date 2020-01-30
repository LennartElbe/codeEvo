import functools
import typing
import string
import random
import pytest

def divisors(x: int) -> list:
    divisors_list = []
    i = 1
    if x == 0:
        return []
    while i <= x:
        if x%i == 0:
            divisors_list.append(x)
            i += 1
        else:
            i += 1
    return divisors_list

print(divisors(4))

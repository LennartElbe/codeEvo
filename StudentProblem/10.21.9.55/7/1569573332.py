import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    return_list = []
    for i in range(1, n+1):
        if n%i == 0:
            return_list.append(i)
        else:
            pass
    return return_list

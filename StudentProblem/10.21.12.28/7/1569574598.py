import functools
import typing
import string
import random
import pytest

def divisors(n :int) -> list:
    ls = []
    count = 1
    ss = n
    while ss != 0:
        if ss % count == 0:
            ls.append(n)
            ss = ss // count
            count = 1
        else:
            count += 1
    return ls

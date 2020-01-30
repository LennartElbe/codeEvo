import functools
import typing
import string
import random
import pytest

def divisors (n):
    result = []
    for i in range (1,n+1):
        if n % i == 0:
            result.append(i)
    return result

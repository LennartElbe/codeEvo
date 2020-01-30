import functools
import typing
import string
import random
import pytest

def divisors(n, d):
    result = []
    if n <= 0:
        return result
    else:
        if n % d != 0:
            continue
        else:
            for i in d:
                

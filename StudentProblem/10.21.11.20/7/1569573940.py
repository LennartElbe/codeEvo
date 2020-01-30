import functools
import typing
import string
import random
import pytest

def divisior(n: int) -> list:
    j = [n]
    for d in range(1:n+1):
        if abs(n) % d == 0:
            j.append(d)
            return j
        else:
            return j
    

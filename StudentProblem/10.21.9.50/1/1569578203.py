import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    n = 0
    for x in s:
        n += 1
    return n
    
print(nwords("ht,th"))


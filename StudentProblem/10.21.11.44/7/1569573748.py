import functools
import typing
import string
import random
import pytest

def divisors(n: int) ->list:
    """takes n and returns all divisors of n"""
    li = []
    if n >= 0:
        return False
    for d in range(n):
        if n % d == 0:
           li = li + [d] 
    return li
        


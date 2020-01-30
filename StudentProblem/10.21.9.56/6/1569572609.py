import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs:list):
    'return the numbers from a given list in a new list ,that grosser oder gleich a given number'
    if xs == []:
        return []
    else:
        res = []
        for i in xs:
            if i <= x:
                res += [i]
        return res        

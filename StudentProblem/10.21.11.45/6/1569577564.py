import functools
import typing
import string
import random
import pytest

def list_filter(x, xs):
    """returns a list from the numbers in the list, wich smaller or the same as x"""
    result = []
    for i in xs : 
        if x > i:
            return result
        else:
            result.append(i)
        return result
            

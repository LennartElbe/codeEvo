import functools
import typing
import string
import random
import pytest

def list_filter(x, xs):
    result = []
    for i in xs : 
        if x > i:
            return result
        else:
            i.append(result)
        return result
            

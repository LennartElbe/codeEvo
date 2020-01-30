import functools
import typing
import string
import random
import pytest

def list_filter(x:int ,xs:list) -> list:
    """returns every number in xs wich is smaller than x
     args: int x
         list xs to pick numbers from
         retrns: every number from xs wich is smaller or epual to x"""
    result = []
    for i in xs:
        if x >= i:
            result.append(i)
    return result

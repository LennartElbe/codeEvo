import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: lst):
    result = []
    for element in xs:
        if element <= x:
            result.append(element)
    return result

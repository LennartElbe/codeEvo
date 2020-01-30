import functools
import typing
import string
import random
import pytest

def list_filter(x, xs):
    """
    """
    result = []
    for element in xs:
        if element <= x:
            result.append(element)
    return result

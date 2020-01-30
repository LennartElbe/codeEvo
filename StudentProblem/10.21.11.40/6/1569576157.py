import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """
    Filters a given list so that any elements greater than x are removed.
    """
    return list(filter(lambda y: y <= x, xs))

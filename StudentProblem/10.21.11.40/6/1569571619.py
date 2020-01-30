import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    return list(filter(lambda y: y <= x, xs))

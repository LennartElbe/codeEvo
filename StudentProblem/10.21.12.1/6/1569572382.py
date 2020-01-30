import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    result = []
    for i in xs:
        if i <= x:
            result.append(i)
    return result

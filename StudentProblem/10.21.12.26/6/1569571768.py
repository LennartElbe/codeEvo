import functools
import typing
import string
import random
import pytest

def list_filter(x:int ,xs:list) -> list:
    result = []
    for i in xs:
        if x > i:
            append.result(i)
    return result

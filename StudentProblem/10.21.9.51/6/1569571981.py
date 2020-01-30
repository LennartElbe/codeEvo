import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list):
    temp_list = []
    for y in xs:
        if y <= x:
            temp_list.append(y)
    return temp_list

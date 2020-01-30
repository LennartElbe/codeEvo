import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    ret_list = []
    for i in xs:
        if i <= x:
            ret_list + list(i)
    return ret_list

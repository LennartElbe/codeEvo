import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    filtered_list = []
    i = 1
    while i < len(xs):
        if xs[i] <= x:
            filtered_list.append(xs[i])
            i += 1
        elif x >= xs[i]:
            i += 1
    return filtered_list

list_filter(5, [1,2,4,5,8,9])

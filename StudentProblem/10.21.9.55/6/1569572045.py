import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    new_list = []
    for i in xs:
        if i <= x:
            new_list.append(i)


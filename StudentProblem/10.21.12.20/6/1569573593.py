import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list):
    same_or_smaller = []
    for i in xs:
        if i <= x:
            same_or_smaller = [same_or_smaller]+[i]
    print(same_or_smaller)

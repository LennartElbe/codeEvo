import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    """berechnet anz worte im string"""
    take = 0
    skip = 0
    for i in s:
        if i not string.whitespace:
            take += 1
        else:
            skip += 1
    res = len(s) - skip
    return res

nwords("Hello world")


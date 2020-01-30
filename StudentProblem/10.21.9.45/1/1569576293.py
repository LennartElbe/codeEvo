import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    """
    Counts the number of words in a string and returns the resulting number.
    s: A given string
    """
    a = len(s)
    res = 0
    for a in range(s):
        if s[a] == string.whitespace:
            res += 1
    return res


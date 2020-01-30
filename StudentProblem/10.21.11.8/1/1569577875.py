import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    """Returns the number of words in a given string.
    Args:
        s: a string
    Returns:
        n: a number
    """
    res = 0
    for elem in s:
        if elem in string.whitespace:
            res += 1
    res += 1
    return res

print(nwords("asd asd asd"))



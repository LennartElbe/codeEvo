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
    for a in range(s + 1):
        if s[a] == string.whitespace:
            res += 1
    return res
def word_count_iter(n: iter) -> str:
    """
    An iterator that returns the number of rows, words and symbols in a given iterable object.
    n: An iterable object
    """
    if len(n) != 0:
        sym = len(n) + 1
        # count up one row, if row length is reached
        if len(n) > 72:
            rows += 1
        words = 0
        for a in len(n + 1):
            if n[a] == string.whitespace:
                words += 1
        return (rows, words, sym)
    else:
        return (0, 0, 0)

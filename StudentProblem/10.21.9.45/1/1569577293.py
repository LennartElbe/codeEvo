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
    rows = enumerate(n)
    sym = len(n)
    for a in range(n + 1):
        

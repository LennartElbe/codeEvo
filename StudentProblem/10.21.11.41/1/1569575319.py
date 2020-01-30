import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    """Function counts words in string. Words are separated with element from string.whitespace.
       Counter is at the beginning 1, because there is for sure one word in string, otherwise zero
       is returned.
    """
    if s == '':
        return 0
    res = 1
    for i in s:
        if i in string.whitespace:
            res += 1
    return res
def word_count_iter(it) -> tuple:
    """returns tuple containing numbers of rows, words and all elements."""
    if it == "":
        return (0, 0, 0)
    rows = 1
    words = 0
    elements = 0
    for i in it:
        elements += 1
    for row in it:
        rows +=1
    words = nwords(it)
    return (rows, words, elements)

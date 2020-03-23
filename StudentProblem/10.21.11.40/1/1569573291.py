import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """
    Determines the amount of words in this string.
    """
    word_count = 1
    for c in s:
        print("-" + c + "-")
        print("-" + string.whitespace + "-")
        if c == string.whitespace:
            word_count += 1
    return word_count
## Lösung Teil 2.
def word_count_iter(it: iter) -> tuple:
    """
    Returns the amount of strings, total words and total characters
    generated by an iterator.
    """
    rows = 0
    words = 0
    characters = 0
    for s in it:
        rows += 1
        words += nwords(s)
        characters += len(s)
    return (rows, words, characters)
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    assert word_count_iter(["foo bar", "baz"]) == (2, 3, 10)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(file) -> tuple:
    with open(file) as fs:
        return word_count_iter(fs)
######################################################################

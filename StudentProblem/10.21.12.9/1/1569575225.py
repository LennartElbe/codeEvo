import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Returns the number of words in s.
    Arguments:
        s: A string
    """
    res = 0
    for letter in s:
        if letter == ' ':
            res += 1
    if s != "":
        res += 1
    return res
## Lösung Teil 2.
def word_count_iter(x) -> tuple:
    """Returns a tuple with the frequency of the lines, the words and the letters.
    Arguments:
        x: A iterable argument
    """
    lines = 0
    words = 0
    letters = 0
    for line in x:
        lines += 1
        words += nwords(line)
        for letter in line:
            if letter != ' ':
                letters += 1
    return (lines, words, letters)

print(word_count_iter(["Hello", "World", "is nice"]))
######################################################################
## Lösung Teil 3. (Tests)
def test_word_count_iter():
    assert word_count_iter([""]) == (1, 0, 0) #Contains a empty line
    assert word_count_iter(["Hello", "World", "is nice"]) == (3, 4, 16)
    assert word_count_iter(["A"]) == (1, 1, 1)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(file: str) -> tuple:
    """Returns a tuple with the frequency of the lines, the words and the letters from the given file (path).
    Arguments:
        file: A filename or a PATH to a file
    """
    reference = open(filename, "r")
    return word_count_iter(reference)
######################################################################

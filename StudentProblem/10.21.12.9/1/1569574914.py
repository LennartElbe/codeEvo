import functools
import typing
import string
import random
import pytest

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
def word_count_iter(x):
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

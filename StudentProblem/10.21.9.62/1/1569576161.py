import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    """Zählt die Anzahl an Wörter von Argument s
    Args:
    s: ist ein String"""
    one_word = ""
    words = []
    for x in s:
        if x is not "":
            one_word += x
        elif x is ""
            words += [one_word]
    return len(words)
def word_count_iter(s: str):
    start = 1
    signs = 0
    for x in s:
        if x is in [";",",",":","."]:
            signs += 1
    yield tuple(start, nwords(x), signs, x)

s = "Hallo 
    World"
print(word_count_iter(s: str))

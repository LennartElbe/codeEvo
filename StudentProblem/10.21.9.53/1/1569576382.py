import functools
import typing
import string
import random
import pytest

def nwords(s) -> int :
    words = 1
    for i in s:
        if i == string.whitespace:
            while i == string.whitespace:
                continue
            words += 1
    return words

def test_nwords_a():
    a = "Das ist ein Test"
    assert nwords(a) == 4


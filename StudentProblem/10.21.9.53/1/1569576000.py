import functools
import typing
import string
import random
import pytest

def nwords(s) -> int :
    words = 1
    text =  list(s)
    for i in text:
        if i is '':
            words += 1
    return words

def test_nwords_a():
    a = "Das ist ein Test"
    assert nwords(a) == 4


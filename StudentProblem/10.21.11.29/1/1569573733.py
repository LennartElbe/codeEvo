import functools
import typing
import string
import random
import pytest

def nwords(s):
    L = list(s)
    return L

def test():
    assert(nwords("Ha ho") == ["H", "a", " ", "h", "o"])


import functools
import typing
import string
import random
import pytest

def nwords(s):
    L = list(s)
    return L

def test_nwords():
    assert (nwords("Ha Ho") == ["H", "a"," ", "H", "o"])

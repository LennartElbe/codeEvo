import functools
import typing
import string
import random
import pytest

def nwords(s:str) -> int:
    result = 0
    k = 0
    for i in range(0, len(s)):
        if s[i] == string.whitespace:
            if k < i - 1:
                result = result + 1
            k = i

def test_nwords():
    assert nword("  ") == 0
    assert nword("  hallo   k  l") == 3


import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    result = []
    for i in s:
        if i == " ":
            x = s.index(i)
            y = s[:x + 1]
            s = s[x + 2:]
            result.append(y)
        else:
            result.append(s)
    return result

def test_11():
    assert nwords("Hallo ") == ["Hallo "]


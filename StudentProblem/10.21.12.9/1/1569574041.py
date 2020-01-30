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
    res += 1
    return res

print(nwords("Hallo, ich bin jetzt da lol."))


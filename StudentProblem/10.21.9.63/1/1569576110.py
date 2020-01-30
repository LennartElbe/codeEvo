import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    c = 0
    for i in range(0, len(s)):
        if i is i.whitespace:
            c = c + 1
    return c
    


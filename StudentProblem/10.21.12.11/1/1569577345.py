import functools
import typing
import string
import random
import pytest

def nwords(s):
    sep = True
    n = 0
    for c in s:
        if c == ' ' and not sep:
            sep = True
            n += 1
        elif c != ' ':
            sep = False
    if not sep:
        n += 1
    return n


print(nwords("   jg   ja n "))


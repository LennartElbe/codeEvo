import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    words = 0
    for n in s:
        if n is string.whitespace:
            words += 1
print(nwords("hallo hallo"))
            
    


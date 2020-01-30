import functools
import typing
import string
import random
import pytest

def nwords_helper(s: str) -> int:
    count = 0
    while s[count] not in string.whitespace:
        count += 1
    if s in string.whiespace:
        return True
    else:
        return False
    
print(nwords_helper("habba ba"))
print(nwords_helper("habba"))


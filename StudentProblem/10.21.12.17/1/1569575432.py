import functools
import typing
import string
import random
import pytest

def nwords_helper(s: str) -> int:
    count = 0
    while s[count] not in string.whitespace and count <= (len(s) - 2):
        count += 1
        print(count)
    if s[count] in string.whitespace:
        return True
    else:
        return False
    
print(nwords_helper("habba ba"))
print(nwords_helper("habba"))


import functools
import typing
import string
import random
import pytest

def nwords_helper(s: str) -> int:
    count = 0
    while s[count] not in string.whitespace and count <= (len(s) -1):
        count += 1
        print(count)
    if s in string.whitespace:
        return True
    else:
        return False
    
print("h" not in string.whitespace)


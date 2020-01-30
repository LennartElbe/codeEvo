import functools
import typing
import string
import random
import pytest

def nwords_helper(s: str) -> int:
    count = 0
    while s[count] not in string.whitespace and count <= (len(s) - 2):
        count += 1
    if s[count] in string.whitespace:
        return count
    else:
        return False
    
def nwords(s: str) -> int:
    if len(s) == 0:
        return 0
    while s[0] in string.whitespace:
        nwords(s[1:])
    if s[0] not in string.whitespace:
        words = 1
        while nwords_helper(s):
            s = s[nwords_helper(s) + 1:]
            words += 1
        return words

print(nwords("habba bubba"))
print(nwords("a a a a a"))
print(nwords(""))
print(nwords(" "))


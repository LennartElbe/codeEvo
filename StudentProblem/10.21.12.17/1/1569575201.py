import functools
import typing
import string
import random
import pytest

def nwords_helper(s: str) -> int:
    count = 0
    print s[count]
    if s[count] in string.whitespace:
        return True
    else:
        return False
    
print(nwords_helper("habba ba"))
print(nwords_helper("habba"))


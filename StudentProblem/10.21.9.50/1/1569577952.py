import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    n = 0
    temp_list = []
    for x in s:
        temp_list.append(x)
    return temp_list
    
print(nwords("ht th"))


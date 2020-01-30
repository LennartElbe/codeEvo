import functools
import typing
import string
import random
import pytest

def is_palindromic (n):
    if n < 0:
        return False
    if n >0 and n < 10:
        return True
    stringy = ""
    stringy = n
    revese = ""
    revese = stringy[::-1]
    b= 0
    for i in stringy:
        b += 1
        if i != stringy[b]:
            break

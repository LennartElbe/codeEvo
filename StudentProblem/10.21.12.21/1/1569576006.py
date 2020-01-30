import functools
import typing
import string
import random
import pytest

def nwords(s: str):
    """berechnet anz worte im string"""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    take = 0
    skip = 0
    for i in s:
        if i not in letters:
            take += 1
        else:
            skip += 1
    res = (len(s) - skip)
    return res

print(len("Hello world"))
print(nwords("Hello world"))


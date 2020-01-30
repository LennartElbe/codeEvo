import functools
import typing
import string
import random
import pytest

def nwords(s: string):
    temp = 0
    anzahl = 0
    for i in string:
        if i == string.whitespace:
            temp += 1


import functools
import typing
import string
import random
import pytest

def leap(x):
    if x % 4 == 0:
        return True
    elif (x % 100 == 0) and (not(x % 400 == 0)):
        return True

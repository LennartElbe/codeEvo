import functools
import typing
import string
import random
import pytest

def leap (x:int)->bool:
    if x < 1582:
        return false


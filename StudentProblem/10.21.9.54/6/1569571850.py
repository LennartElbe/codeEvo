import functools
import typing
import string
import random
import pytest

def list_fil(x: int, xs: list)->list:
    return [a for a in xs if a <= x]

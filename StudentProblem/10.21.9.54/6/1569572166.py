import functools
import typing
import string
import random
import pytest

def list_filter(x: int,xs: list) -> list:
    return [a for a in xs if a <= x]

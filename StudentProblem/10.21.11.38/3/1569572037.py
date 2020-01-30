import functools
import typing
import string
import random
import pytest

def leap(n: int) -> bool:
    if n % 4 == 0:
        return True
    elif n % 100 == 0:
        return False
    elif n % 400 == 0:
        return True

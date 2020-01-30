import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    if n <= 0:
        print("Enter positive number")
    else n.__invert__ == n:
        return True

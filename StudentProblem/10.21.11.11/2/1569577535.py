import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    if n <= 0:
        print("Enter positive number")
    else:
        n = str(n)
        print(n)
    return n     

n = 5
n = str(n)
print(n)

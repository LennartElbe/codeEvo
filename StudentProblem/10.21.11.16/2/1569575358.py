import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    if n == n[:]:
        return True
    else:
        return False
    

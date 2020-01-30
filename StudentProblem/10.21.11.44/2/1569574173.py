import functools
import typing
import string
import random
import pytest

def is_palindromic(n : int) -> bool:
    m = n[::-1] 
    if n == m:
        return "Palindrom"
    else:
        return "kein Palindrom"
    

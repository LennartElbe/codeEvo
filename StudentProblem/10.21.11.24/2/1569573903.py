import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Testet eine postive ganze Zahl, ob sie palindromic ist
    Arg: n: int
    Return: Bool True, wenn palindromic
            None, wenn n <= 0
    """
    if n <= 0:
        return None
    else:
        s = str(n)
        cs = s[-1::]
        if s == cs:
            return True
        else:
            return False
        

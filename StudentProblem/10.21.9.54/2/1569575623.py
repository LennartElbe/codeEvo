import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int)-> bool:
    if n <= 0:
        return ("Falsche Eingabe")
    else:
        a = str(n)
        if a == a[-1::-1]:
            return True
        else:
            False
    

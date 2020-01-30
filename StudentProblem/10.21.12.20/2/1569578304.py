import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
#Testet ob die ganzzahlige Zahl n ein Palindrom ist. Gibt True oder False zurück
    n_str = str(n)
    if n_str == n_str[-1::-1]:
        return True
    else:
        return False

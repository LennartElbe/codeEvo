import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    if year % 4 == 0:
        return True
    elif year % 100 == 0 and year % 400 != 0:
        return False
    
leap(2016)

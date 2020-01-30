import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    if year <= 1582:
        return False
    elif year % 4 == 0 and not(year % 100 == 0 and not year % 400  == 0):
        return True
    else:
        return False
    
print(leap(2000))

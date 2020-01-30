import functools
import typing
import string
import random
import pytest

def leap(jahreszahl: int) -> bool:
    if jahreszahl % 4 == 0:
        return True
    elif (jahreszahl % 100 == 0) and (jahreszahl % 400 != 0) and (jahreszahl > 1582):
        return False 

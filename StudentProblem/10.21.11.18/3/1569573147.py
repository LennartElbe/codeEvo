import functools
import typing
import string
import random
import pytest

def leap(year) -> int:
    year >= 1582
    if year % 400 == 0:
        return print("False")
    elif year % 100 == 0:
        return print("True")
    elif year % 4 == 0:
        return print("True")
    else:
        print("Kein Schaltjahr")

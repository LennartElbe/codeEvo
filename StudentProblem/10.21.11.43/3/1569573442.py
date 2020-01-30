import functools
import typing
import string
import random
import pytest

def leap(year : int) -> str:
    year >= 1582
    if year % 4:
        if year % 400:
            if year % 100:
                return 'No leap year'
            else:
                return 'leap year'
    else:
        return 'No leap year'

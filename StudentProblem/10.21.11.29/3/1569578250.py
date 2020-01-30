import functools
import typing
import string
import random
import pytest

def leap(year):
    """ 
    Args:
        year: Int
    Diese Funktion ergibt für ein eingegebenes jahr ob es ein Schaltjahr ist oder nicht.
    Return: False
            True"""
    n = year
    n < 1582:
        return False
    if n % 4 == 0:
        if n % 100 == 0:
            return False
        elif n % 400 == 0:
            return True
    else:
        return False

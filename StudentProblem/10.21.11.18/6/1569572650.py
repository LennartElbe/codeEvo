import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Funktion, a Number of Interger and a list of Numbers, 
    to to combine the number and the list in one list"""
    xs = []                 
    try:
        x <= str(xs)
        return xs
    
                  # returned the list, if the Elements in xs are <= x
    

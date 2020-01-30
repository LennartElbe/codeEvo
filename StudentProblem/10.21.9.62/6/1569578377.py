import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list):
    """gibt die Liste aller Elemente aus xs zurück, die kleiner oder gleich x sind.
    Args: 
    x: ist eine Zahl
    xs: liste von Zahlen"""
    res = [y for y in xs if y <= x]
    return res


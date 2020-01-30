import functools
import typing
import string
import random
import pytest

def list_filter(x, xs):
    """
    Args:
    x: Int
    xs: List
    Diese funktion returnt die werte der liste, welche kleiner als x sind.
    
    Return: list"""
    L = []
    for i in xs:
        if i <= x:
            L.append(i)
    return L

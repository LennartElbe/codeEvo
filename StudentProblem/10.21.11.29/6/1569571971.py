import functools
import typing
import string
import random
import pytest

def list_filter(x, xs):
    """ 
    x: Int
    xs: List
    Diese funktion returnt die werte der liste, welche kleiner als x sind.
    L = []
    for i in xs:
        if x <= i:
            L.append(i)

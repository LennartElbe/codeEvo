import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Filtert eine Liste und gibt die Werte kleiner gleich x zurück"""
    returnlist = []
    for i in xs:
        if i <= x:
            returnlist.append(i)
    return returnlist

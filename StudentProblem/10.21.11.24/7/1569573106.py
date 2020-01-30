import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """Gibt alle Divisoren einer zahl zurück
    Arg: n: int > 0
    Return: list von allen teilern
            None falls n <= 0
    """
    if n <= 0:
        return None
    else:
        returnlist = []
        for i in range(1, n+1):
            if n % i == 0:
                returnlist.append(i)
        return returnlist

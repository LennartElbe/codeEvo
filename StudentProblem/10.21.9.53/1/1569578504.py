import functools
import typing
import string
import random
import pytest

def nwords(s) -> int :
    """
        Zählt die Anzahl der Worte in einem String. Worte sind durch string.whitespace
        getrennt.
    """
    words = 1
    for i in s:
        if i == string.whitespace:
            words += 1
    return words




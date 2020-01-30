import functools
import typing
import string
import random
import pytest

def nwords(s:string)-> int:
    """
        Args:
            s string
        return
            number of words
    """
    return s.split(" ")


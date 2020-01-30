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
    return s.string.whitespace()
def test_nwords():
    assert nwords("hello world") == 2

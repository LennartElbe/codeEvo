import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    """Function to compute the number of words in a string.
    
    Args:
        s(str): A given string.
        
    Returns:
        r(int): Number of words in the string.
    """
    res = []
    for element in s:
        res.append(element)
    return len(res)


def word_count_iter():
    """
    """

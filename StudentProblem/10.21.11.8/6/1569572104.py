import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Returns a list of all elements that are smaller or equal to x.
        Args:
        x: an integer
        xs: a list of integers
        
        Returns:
        all elements that are smaller or equal to x
        """
    return[num for num in xs if num <=x]


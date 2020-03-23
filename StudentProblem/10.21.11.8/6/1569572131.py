import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Returns a list of all elements that are smaller or equal to x.
        Args:
        x: an integer
        xs: a list of integers
        
        Returns:
        all elements that are smaller or equal to x
        """
    return[num for num in xs if num <=x]

######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    assert list_filter(3, [1,2,3,4,5]) == [1,2,3]
    assert list_filter(2, [4,5,6]) == []
    assert list_filter(5, [1,2,3]) == [1,2,3]
######################################################################

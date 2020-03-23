import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Function to filter elements out of a list.
    
    Args:
        x(int): Given number
        xs(list): Given list with numbers
        
    Return:
        res(list): A list only containing the elements of xs that are <= x
    """
    res = []
    for i in xs:
        if i <= x:
            res.append(x)
    return res
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    """
    """
    testlist1 = [1, 2, 3, 4, 5, 6]
    testlist2 = [3, 4, 5, 6, 7, 8]
    assert list_filter(3, [1, 2, 3, 4, 5, 6]) == [1, 2, 3]
    assert list_filter(2, testlist2) == []

######################################################################

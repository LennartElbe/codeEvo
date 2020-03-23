import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
def list_filter(x: int, xs: list) -> list:
    """Function to filter elements of a list that are <= a given number.
    
    Args:
        x(int): Given number
        xs(list): Given list containing numbers
        
    Returns:
        res(list): A list only containing the elements of xs that are <= x
    """
    res = []
    for i in xs:
        if i <= x:
            res.append(i)
    return res
######################################################################
# Lösung Teil 2. (Test)

def test_list_filter():
    testlist1 = [1, 2, 3, 4, 5, 6]
    testlist2 = [3, 4, 5, 6, 7, 8]
    assert list_filter(3, testlist1) == [1, 2, 3]
    assert list_filter(2, testlist2) == []

######################################################################

import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Function to filter elements of a list.
    
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

testlist = [1, 2, 3, 4, 5, 6]
list_filter(3, testlist)

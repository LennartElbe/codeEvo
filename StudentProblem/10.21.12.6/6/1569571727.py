import functools
import typing
import string
import random
import pytest

# Lösung Teil 1.
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
######################################################################
# Lösung Teil 2. (Test)


######################################################################

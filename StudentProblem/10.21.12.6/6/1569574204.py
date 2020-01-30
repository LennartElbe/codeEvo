import functools
import typing
import string
import random
import pytest

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

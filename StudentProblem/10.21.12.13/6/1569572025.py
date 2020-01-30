import functools
import typing
import string
import random
import pytest

def list_filter(x: int, xs: list) -> list:
    """Function to filter a given list to a given Argument
    args: x: int which gives the variable to comparte the list with
          xs: the list which will get filterd
    returns: list_filter(1,[]) == []
    """
    res = []
    if xs == []:
        return []
    else:
        for i in xs:
            if i <= x:
                res += [i]
        return res

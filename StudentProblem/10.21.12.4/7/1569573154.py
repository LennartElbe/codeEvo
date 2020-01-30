import functools
import typing
import string
import random
import pytest

def divisors(n: int)-> list:
    """die eine positive ganze Zahl n als Argument nimmt und die Liste aller ihrer Teiler ohne Wiederholung zurückliefert.
    args:
        n (int): Ganze Zahl
    return:
        Eine Liste mit aller Teiler von n
    
    """
    result = []
    for teiler in range(n+1):
        if n % teiler == 0:
            result.append(teiler)
    return result

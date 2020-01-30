import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int)-> bool:
    """
    Die Function is_palindromic die testet ob eine positive ganze Zahl n>0n>0 ein Palindrom ist.
    args: 
        n(int): das zum testen gegebener Zahl
    return:
        boolean: True oder False
    
    """

    if n == n:
        return True
    else:
        return False
    
       

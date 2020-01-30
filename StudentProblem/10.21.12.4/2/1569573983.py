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
    if n < 0:
        return False
    number = str(n)
    elif number == number[-1::-1]:
        return True
    else:
        return False
    
       

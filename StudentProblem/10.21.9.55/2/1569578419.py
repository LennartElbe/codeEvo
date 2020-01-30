import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int)-> bool: 
    """
        Args:
            n: int Ganze Zahl > 0
        return:
            bool: ist die Zahl ein Palindrom
    """
    n_list = str(n).split() 
    for i in range(len(n_list)):
        if n_list[i] == n_list[len(n_list)-i]:
            pass
        else: 
            return False
    return True

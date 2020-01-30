import functools
import typing
import string
import random
import pytest

def divisors(n) -> list:
    """
        
    """
    ret_list = []
    i = 0
    while (i <= n):
        if (n % i) == 0:
            ret_list.append(i)
        i += 1
    return ret_list
        

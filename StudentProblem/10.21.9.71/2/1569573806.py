import functools
import typing
import string
import random
import pytest

def is_palindromic(x:int) -> bool:
    l = list(x)
    for i in range(0, int((len(l)/2) + 1)):
            if not(l[i] == l[len(l) - i]):
                return False
    return True
                
        

import functools
import typing
import string
import random
import pytest

def is_palindromic(x:int) -> bool:
    k = str(x)
    l = list(k)
    for i in range(0, int((len(l)/2))):
            if not(l[i] == l[len(l) - i - 1]):
                return False
    return True
                
        

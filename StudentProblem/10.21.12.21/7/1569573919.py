import functools
import typing
import string
import random
import pytest

def divisors(n: int):
    """n ganze Zahl > 0, retrun liste aller teiler von n
    16: 4, 2, 16, 1, 
    
    """
    res = []
    if n > 0:
        for i in range(0, n):
            if n // i:
                res.append(1)
            else:
                continue
    else:
        return None
                
        

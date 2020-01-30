import functools
import typing
import string
import random
import pytest

def divisors(n)
    """
    Nimmt positive ganze Zahl und gibt die Listee aller ihrer Teiler ohne wiederholung zurück
    
    args:
        n: int (positives integer)
       
    returns:
        result: lst (aller Teiler ohne Wdh)
    """
    result = []
    if n == 0 or type(n) != int:
        return "Nanana"
    else:
        for i in range(1, n + 1):
            if n % i == 0 and i not in result:
                result.append(i)
    return result

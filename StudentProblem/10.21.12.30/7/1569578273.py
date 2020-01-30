import functools
import typing
import string
import random
import pytest

def divisors(n: int) -> list:
    """" Berechnung der Menge von Teilern einer positiven nganzen Zahl 
    """"
    
    if n<=0:
        return
    list_d = []
    d = 1
    while d <= n:
        if n % d == 0:
            return list_d.append(d)
        
